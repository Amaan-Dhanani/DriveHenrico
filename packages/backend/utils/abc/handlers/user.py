# === Core ===
from pydantic import Field
from secrets import token_hex
from utils.abc.handlers.base import WrapperModel
from datetime import datetime, timezone, timedelta

# === Database ===
from pymongo.collection import Collection
from utils.mongo.Client import MongoClient

# === Types ===
from typing import ClassVar, Union


class User(WrapperModel):
    email: str
    id: str = Field(default_factory=lambda: token_hex(32))
    verified: bool = False
    account_type: str = ""
    ttl: Union[int, None] = None
    __collection__: ClassVar[Collection] = MongoClient.users

    @classmethod
    def after_create(cls, instance: "User") -> "User":
        """
        Post-creation hook that adds a TTL (time-to-live) if the user is unverified.

        This method is invoked automatically after creating a new model instance using
        the `create` method. If the user is not verified and no TTL is already set,
        it assigns a TTL 10 minutes from the current UTC time. This TTL can later be used
        to expire or clean up unverified accounts.

        :returns User: The modified model instance with TTL set if applicable
        """

        if not instance.verified and instance.ttl is None:
            # Generate TTL
            time_delta = int((datetime.now(timezone.utc) + timedelta(seconds=1)).timestamp())
            instance.ttl = time_delta

        return instance

    @property
    def expired(self) -> bool:
        """
        Indicates whether the user account is expired based on the TTL.

        A user is considered expire-able if:
        - They are not verified
        - A TTL value exists

        A user is considered expired if:
        - The current UTC time is greater than or equal to the TTL timestamp

        :returns bool: True if the user is expired, False otherwise
        """

        # If its verified or no ttl is specified
        if self.verified or self.ttl is None:
            return False

        # If current time hasn't passed (is smaller) than defined ttl
        if datetime.now(timezone.utc) < datetime.fromtimestamp(self.ttl):
            return True

        return True
