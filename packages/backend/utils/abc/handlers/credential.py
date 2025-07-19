# === Core ===
from hashlib import sha512
from secrets import token_hex
from utils import WrapperModel

# === Database ===
from pymongo.collection import Collection
from utils.mongo.Client import MongoClient

# === Types ===
from typing import ClassVar, Self
from utils.abc import User

class Credential(WrapperModel):
    account_id: str
    email: str 
    salt: str
    hashed: str
    __collection__: ClassVar[Collection] = MongoClient.credentials
    
    @classmethod
    def from_user(cls, user: User, password: str) -> Self:
        """
        Creates a new Credential object from a User and raw password

        Hashes the password using a generated salt and SHA-512, then returns
        a new Credential model instance (does not insert it into the database).

        :param User user: The associated User object
        :param str password: The raw password to be salted and hashed
        :returns Credential: The generated Credential object
        """
        
        salt = token_hex(32)
        hashed = sha512((password+salt).encode("utf-8")).hexdigest()
        
        return cls(
            account_id=user.id,
            email=user.email,
            salt=salt,
            hashed=hashed
        )