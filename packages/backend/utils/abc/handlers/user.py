# === Core ===
from pydantic import Field
from secrets import token_hex
from utils.abc.handlers.base import WrapperModel

# === Database ===
from pymongo.collection import Collection
from utils.mongo.Client import MongoClient

# === Types ===
from typing import ClassVar

class User(WrapperModel):
    email: str
    id: str = Field(default_factory=lambda: token_hex(32))
    verified: bool = False
    account_type: str = ""
    __collection__: ClassVar[Collection] = MongoClient.users