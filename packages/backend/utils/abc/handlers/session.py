# === Core ===
from secrets import token_hex
from dataclasses import asdict, dataclass, field
from pymongo.collection import Collection

# === Database ===
from utils.mongo.Client import MongoClient
collection: Collection = MongoClient.sessions

# === Types ===
from ..types.session import T_Session
from ..handlers.user import User

@dataclass
class Session:
    account_id: str    
    id: str = field(default_factory=lambda: token_hex(64))

    @classmethod
    def create(cls, user: User):
        buff: T_Session = {
            "account_id": user.id,
            "id": token_hex(64)
        }
        return cls(**buff)
    
    @classmethod
    def exists(cls, id: str):
        if not collection.find_one({"id": id}):
            return False
        return True
    
    @classmethod
    def delete(cls, id: str):
        return collection.delete_one({"id": id})
    
    def insert(self):
        collection.insert_one(asdict(self))
        return self 