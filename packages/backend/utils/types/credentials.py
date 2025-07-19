import hashlib
import random
import secrets
from typing import TypedDict
from dataclasses import dataclass

class CredentialsDict(TypedDict):
    email: str
    hashed: str
    salt: str
    _id: str
    
@dataclass
class Credentials:
    email: str
    hashed: str
    salt: str = secrets.token_hex(32)
    _id: str = f"unbound_{secrets.token_hex(8)}"
    
    @classmethod
    def create(cls, data: CredentialsDict) -> "Credentials":
        """
        Creates a credential object and returns itself in a dataclass object
        """
            
        return cls(**data)
