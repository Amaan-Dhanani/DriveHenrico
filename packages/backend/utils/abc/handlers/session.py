# === Core ===
from pydantic import Field
from secrets import token_hex
from utils.abc.handlers.base import WrapperModel
from utils.abc.handlers.user import User

# === Database ===
from pymongo.collection import Collection
from utils.mongo.Client import MongoClient

# === Types ===
from typing import ClassVar, Self

class Session(WrapperModel):
    account_id: str
    id: str = Field(default_factory=lambda: token_hex(32))
    __collection__: ClassVar[Collection] = MongoClient.sessions

    @classmethod
    def from_user(cls, user: User) -> Self:
        """
        Creates a new session model instance from a given user object

        Initializes a `Session` using the `id` of the provided `User` instance
        as the `account_id`. A new random session ID will be generated automatically.

        :param User user: The user instance to associate the session with
        :returns Self: A new session model instance
        """
        return cls(
            account_id=user.id
        )
