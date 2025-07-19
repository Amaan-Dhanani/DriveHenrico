# === Core ===
from secrets import token_hex
from dataclasses import asdict, dataclass, field
from typing import Any, Mapping, Optional
from pymongo.collection import Collection

# === Database ===
from utils.mongo.Client import MongoClient
collection: Collection = MongoClient.users

# === Types ===
from ..types.user import T_User

@dataclass(init=False)
class User:
    email: Optional[str] = None
    id: str = field(default_factory=lambda: token_hex(32))
    verified: bool = False
    account_type: str = ""
    
    def __init__(self, **kwargs) -> None:
        self.email = kwargs.get("email")
        self.id = kwargs.get("id", token_hex(32))
        self.verified = kwargs.get("verified", False)
        self.account_type = kwargs.get("account_type", "")
        self._id = kwargs.get("_id")
        
    @classmethod
    def get(cls, id: str):
        search = collection.find_one({"id": id})
        if not search:
            raise LookupError(f"User doesn't exist, id: {id}")
        return cls(**search)

    @classmethod
    def create(cls, data: T_User):
        return cls(**data)
    
    @classmethod
    def email_exists(cls, email: str):
        if not collection.find_one({"email": email}):
            return False
        return True
    
    @classmethod
    def exists(cls, id: str):
        if not collection.find_one({"id": id}):
            return False
        return True
    
    def delete(self):
        return collection.delete_one({"id": self.id})
    
    def insert(self):
        collection.insert_one(asdict(self))
        return self 
    
    def update(self, operation: str, update: Mapping[str, Any]):
        return collection.update_one({"id": self.id}, {operation: update})