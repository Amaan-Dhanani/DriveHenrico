# === Core ==
import random
from pydantic import Field
from secrets import token_hex
from datetime import datetime, timedelta, timezone

# === Utils ===
from utils.abc.handlers.base import WrapperModel
from utils.abc.handlers.user import User
from utils.console import console
from utils.email import CodeEmail

# === Database ===
from pymongo.collection import Collection
from utils.mongo.Client import MongoClient

# === Types ===
from typing import ClassVar, Optional, Self, Union


class ChallengeAttempt:
    """
    Handles a single challenge validation attempt.

    This class is responsible for verifying a user's attempt against a given challenge.
    It provides utilities to check whether the attempt is valid, expired, or has exceeded
    the allowed number of tries. When used as a context manager, it will automatically
    clean up the challenge from the database if necessary.

    :param Challenge challenge: The original challenge object this attempt is based on.
    :param Union[str, None] value: The value provided by the user for verification.

    Attributes
    ----------
    value : Union[str, None]
        The user's input for the challenge.
    challenge : Challenge
        The original Challenge instance tied to this attempt.
    
    Behavior
    --------
    - On context manager exit, deletes the challenge if it's expired or has too many failed attempts.
    - Provides properties for:
        - `ok`: True if the attempt is valid.
        - `expired`: True if the challenge is past its expiration timestamp.
        - `incorrect`: True if the provided value doesn't match.
        - `too_many_attempts`: True if the max allowed attempts has been exceeded.
    """

    def __init__(self, challenge: "Challenge", value: Union[str, None] = None):
        self.value = value
        self.challenge = challenge
        self._inc_attempts()

    def __enter__(self):
        """
        Enables use of the ChallengeAttempt instance as a context manager.

        This allows for automatic resource cleanup (e.g., deleting the challenge from the database)
        when exiting the context block.

        :returns ChallengeAttempt: The current instance
        """
        return self

    def __exit__(self, *_, **__):
        """
        Triggered automatically when exiting a context block.

        Calls internal cleanup logic to remove the challenge if it is expired
        or has exceeded the allowed number of attempts.
        """
        self._cleanup()

    def _cleanup(self):
        """
        Performs cleanup logic for the challenge.

        If the challenge still exists and has either expired or exceeded the max number
        of attempts, it is deleted from the database.
        """
        if not self.exists:
            return
        if self.expired or self.too_many_attempts:
            console.debug(f"Cleaning Up Challenge {self.challenge.challenge_id}")
            self.challenge.delete()

    def _inc_attempts(self) -> None:
        """
        Increments the number of attempts made on the challenge both in memory
        and in the database.
        """
        self.challenge.attempts += 1
        console.debug(f"Attempt: {self.challenge.attempts}/{self.challenge.max_attempts}, too_many?: {self.too_many_attempts}")
        
        MongoClient.challenge.update_one({"challenge_id": self.challenge.challenge_id}, {"$inc": {"attempts": 1}})

    @property
    def ok(self) -> bool:
        return not self.incorrect and not self.expired and not self.too_many_attempts

    @property
    def too_many_attempts(self) -> bool:
        return self.challenge.attempts >= self.challenge.max_attempts

    @property
    def incorrect(self) -> bool:
        return self.challenge.value != self.value

    @property
    def expired(self) -> bool:
        now = int(datetime.now(timezone.utc).timestamp())
        return (self.challenge.expires_at or 0) < now

    @property
    def exists(self) -> bool:
        return self.challenge.exists(challenge_id=self.challenge.challenge_id)


class Challenge(WrapperModel):
    challenge_id: str = Field(default_factory=lambda: token_hex(64))
    value: Union[str, None] = None
    user_id: str
    type: str
    method: str
    attempts: int = 0
    max_attempts: int
    expires_at: Union[int, None] = None

    __collection__: ClassVar[Collection] = MongoClient.challenge

    @classmethod
    def from_user(cls, user: User, value: Optional[str] = None, type: str = "code", method: str = "email", max_attempts: int = 5) -> Self:
        """
        Creates a challenge object from a user object.

        :param User user: User object
        :param Optional[str] value: Value of the challenge object if applicable
        :param str type: Input type of challenge
        :param str method: Method of the challenge (How the user should get the value)
        :param int max_attempts: Maximum attempts of the challenge.
        """

        if type == "code" and not value:
            value = "".join(random.choices('0123456789', k=6))

        expires_at = int((datetime.now(timezone.utc) + timedelta(minutes=10)).timestamp())

        return cls(
            value=value,
            user_id=user.id,
            type=type,
            method=method,
            max_attempts=max_attempts,
            expires_at=expires_at
        )

    def attempt(self, value: Union[str, None]) -> ChallengeAttempt:
        return ChallengeAttempt(self, value)

    async def send(self) -> None:
        """
        Sends the challenge to the user. Depending on the method specified in the challenge,
        the user will either get an email [or a sms message if I ever implement that]
        """

        if self.method == "email":
            console.debug(f"Code sent to {self.user.email} is {self.value}")
            await CodeEmail(to=self.user.email, code=self.value).send()

    @property
    def user(self) -> User | None:
        """
        Attempts to get the user attached to this challenge

        :returns User | None: User if its found, None if not found
        """
        try:
            return User.get(id=self.user_id)
        except Exception as e:
            console.debug(f"Challenge.user Failed {e}")
            return None
