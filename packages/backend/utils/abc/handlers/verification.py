# === Core ===
import random
from secrets import token_hex
from dataclasses import asdict, dataclass, field
from typing import Optional
from pymongo.collection import Collection

# === Database ===
from utils.mongo.Client import MongoClient
collection: Collection = MongoClient.verification

# === Types ===
from ..types.verification import T_Verification
from ..handlers.user import User

def generate_code() -> str:
    return "".join(random.choices('0123456789', k=6))

@dataclass
class Verification:
    account_id: str    
    id: str = field(default_factory=lambda: token_hex(48))
    code: str = field(default_factory=lambda: generate_code())
    _id: Optional[str] = None
    
    @classmethod
    def get(cls, id: str):
        search = collection.find_one({"id": id})
        if not search:
            raise KeyError(f"Verification Object with id not found: {id}")
        return cls(**search)

    @classmethod
    def create(cls, user: User):
        buff: T_Verification = {
            "account_id": user.id,
            "id": token_hex(48)
        }
        
        return cls(**buff)
    
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