# === Core ===
import random
import string
from pydantic import Field
from secrets import token_hex

# === Utils ===
from utils.helper.time import now
from utils.abc.handlers.user import User
from utils.abc.handlers.base import WrapperModel

# === Database ===
from pymongo.collection import Collection
from utils.mongo.Client import MongoClient

# === Types ===
from typing import ClassVar, List, Optional, Self


class Class(WrapperModel):
    name: Optional[str] = None
    
    teacher_id: str
    student_ids: List[str] = []
    invite_code: Optional[str] = None
    
    created_at: Optional[int] = Field(default_factory=lambda: now())
    updated_at: Optional[int] = Field(default_factory=lambda: now())
    
    __collection__: ClassVar[Collection] = MongoClient.classes
    id: str = Field(default_factory=lambda: token_hex(32))

    @classmethod
    def after_create(cls, instance: "Class") -> "Class":
        """
        Post-creation hook that updates the invite_code if its not given
        """
        
        if instance.invite_code is None:
            instance.invite_code = "".join(random.choices(string.ascii_uppercase+string.digits, k=6))
        
        return instance
    
    @classmethod
    def from_user(cls, user: User, name: str) -> Self:
        """
        Creates a new Class object from a user and a class name
        The user must be a teacher

        :param User user: The associated user object
        :param str name: THe name of the new class
        """
        
        if not user.is_teacher:
            raise TypeError("User isn't a teacher")
        
        return cls(
            name=name,
            teacher_id=user.id
        )