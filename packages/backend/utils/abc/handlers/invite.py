# === Core ===
from datetime import timedelta
import random
import string
from pydantic import Field
from secrets import token_hex

# === Utils ===
from utils.helper.time import now, future
from utils.abc.handlers.user import User
from utils.abc.handlers.base import WrapperModel


# === Database ===
from pymongo.collection import Collection
from utils.mongo.Client import MongoClient

# === Types ===
from typing import ClassVar, List, Literal, Optional, Self

class Invite(WrapperModel):
    type: Literal["class", "parent"]
    code: str = Field(default_factory=lambda: Invite.generate_code())
    
    created_by: str
    created_at: int = Field(default_factory=lambda: now())
    expires_at: int
    
    target_parent_id: Optional[str] = None
    
    __collection__: ClassVar[Collection] = MongoClient.invites
    id: str = Field(default_factory=lambda: token_hex(32))
    
    @property
    def parent(self) -> User | None:
        """
        Attempts to get the parent attached to this session
        
        :returns User | None: If the user is found, otherwise None
        """
        
        if self.target_parent_id is None:
            return None
        
        try:
            return User.get(id=self.target_parent_id)
        except LookupError as e:
            return None
    
    @classmethod
    def generate_code(cls) -> str:
        return "".join(random.choices(string.ascii_uppercase+string.digits, k=6))
    
    @classmethod
    def from_user(cls, user: User) -> Self:
        """
        Creates an invite using a specific user
        """
        cls = cls.after_create(cls)
        cls.created_by = user.id
        
        if user.is_parent:
            cls.target_parent_id = user.id
        
        return cls

    @classmethod
    def after_create(cls, instance: "Invite") -> "Invite":
        
        # Handle expires_at
        match instance.type:
            case "class":
                instance.expires_at = None
            case "parent":
                instance.expires_at = future(timedelta(days=7))
            case _:
                instance.expires_at = now()
                
        return instance