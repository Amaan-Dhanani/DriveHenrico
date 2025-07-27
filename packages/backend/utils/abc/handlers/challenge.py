# === Core ==
import random
from pydantic import Field
from secrets import token_hex

# === Utils ===
from utils.abc.handlers.base import WrapperModel
from utils.abc.handlers.user import User
from utils.console import console

# === Database ===
from pymongo.collection import Collection
from utils.mongo.Client import MongoClient

# === Types ===
from typing import ClassVar, Self, Union

class Challenge(WrapperModel):
    challenge_id: str = Field(default_factory=lambda: token_hex(64))
    value: Union[str, None] = None   
    user_id: str
    type: str
    method: str
    attempts: int = 0
    max_attempts: int
    expires_at: Union[int, None] = None
    
    __collection__: ClassVar[Collection] = MongoClient.challenge
    
    @classmethod
    def from_user(cls, user: User) -> Self:
        value = "".join(random.choices('0123456789', k=6))
        
        expires_at = 
        
        return cls(
            value=value,
            user_id=user.id,
            type="code",
            method="email",
            max_attempts=5,
            expires_at=2            
        )
            
        
    @property
    def user(self) -> User | None:    
        """
        Attempts to get the user attached to this challenge
        
        :returns User | None: User if its found, None if not found
        """    
        try:
            return User.get(id=self.user_id)
        except Exception as e:
            console.debug(f"Challenge.user Failed {e}")
            return None