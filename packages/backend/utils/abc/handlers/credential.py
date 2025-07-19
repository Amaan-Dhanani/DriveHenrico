# === Core ===
from secrets import token_hex
from hashlib import sha512
from dataclasses import asdict, dataclass
from pymongo.collection import Collection

# === Database ===
from utils.mongo.Client import MongoClient
collection: Collection = MongoClient.credentials

# === Types ===
from ..types.credential import T_Credential
from ..handlers.user import User


@dataclass
class Credential:
    account_id: str
    email: str

    salt: str
    hashed: str

    @classmethod
    def create(cls, user: User, password: str):

        salt: str = token_hex(64)
        buff: T_Credential = {
            "account_id": user.id,
            "email": user.email,
            "salt": salt,
            "hashed": sha512((password + salt).encode("utf-8")).hexdigest()
        }

        return cls(**buff)

    @classmethod
    def exists_email(cls, email: str):
        if not collection.find_one({"email": email}):
            return False
        return True

    @classmethod
    def exists_account(cls, account_id: str):
        if not collection.find_one({"account_id": account_id}):
            return False
        return True

    @classmethod
    def delete(cls, account_id: str):
        return collection.delete_one({"account_id": account_id})
    
    def insert(self):
        collection.insert_one(asdict(self))
        return self 