# === Core ===
import random
from secrets import token_hex
from pydantic import Field
from utils.abc.handlers.base import WrapperModel
from utils.abc.handlers.user import User

# === Database ===
from pymongo.collection import Collection
from utils.mongo.Client import MongoClient

# === Types ===
from typing import ClassVar, Self

class Verification(WrapperModel):
    account_id: str
    id: str = Field(default_factory=lambda: token_hex(64)) 
    code: str
    __collection__: ClassVar[Collection] = MongoClient.verification
    
    @classmethod
    def from_user(cls, user: User) -> Self:
        """
        Creates a Verification instance from a User object

        Generates a new 6-digit numeric code and binds it to the provided User's account ID.
        This method does not insert the document into the database.

        :param User user: User object to associate with the verification entry
        :returns Verification: Unsaved Verification instance with a generated code
        """

        code = "".join(random.choices('0123456789', k=6))
        
        return cls(
            account_id=user.id,
            code=code
        )