import secrets
from typing import TypedDict
from dataclasses import dataclass


class UserDict(TypedDict):
    email: str
    account_type: str
    verified: bool
    _id: str

@dataclass
class User:
    email: str
    account_type: str
    verified: bool = False
    _id: str = f"user_{secrets.token_hex(64)}"
    
    @classmethod
    def create(cls, data: UserDict) -> "User":
        """
        Creates a user and returns itself in a dataclass object
        """
        return cls(**data)
