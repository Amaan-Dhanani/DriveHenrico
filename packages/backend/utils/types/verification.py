import random
import secrets
from typing import TypedDict
from dataclasses import dataclass

class VerificationDict(TypedDict):
    account_id: str
    code: str
    _id: str
    
@dataclass
class Verification:
    account_id: str
    code: str = "".join(random.choices('0123456789', k=6))
    _id: str = f"verification_{secrets.token_hex(64)}"

    @classmethod
    def create(cls, data: VerificationDict) -> "Verification":
        """
        Creates a verification object and returns itself in a dataclass object
        """
        return cls(**data)
