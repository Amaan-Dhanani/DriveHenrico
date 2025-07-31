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
    invite_code: Optional[str] = Field(default_factory=lambda: Class.generate_code())
    
    created_at: Optional[int] = Field(default_factory=lambda: now())
    updated_at: Optional[int] = Field(default_factory=lambda: now())
    
    __collection__: ClassVar[Collection] = MongoClient.classes
    id: str = Field(default_factory=lambda: token_hex(32))
    
    @classmethod
    def generate_code(cls) -> str:
        return "".join(random.choices(string.ascii_uppercase+string.digits, k=6))
    
    def has_user(self, user_id: str) -> bool:
        """
        Checks if a user is already part of this class
        :returns bool: True if the user is part, else false 
        """
        return user_id in self.student_ids
    
    def add_user(self, user_id: str):
        """
        Adds a user to self.student_ids and updates the document within the database
        """
        self.student_ids.append(user_id)
        self.update({"id": self.id}, "$addToSet", {"student_ids": user_id})
        
    def refresh_invite_code(self) -> None:
        """
        Updates the current invite_code
        """
        
        self.invite_code = self.generate_code()
        self.update({"id": self.id}, "$set", {"invite_code": self.invite_code})

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