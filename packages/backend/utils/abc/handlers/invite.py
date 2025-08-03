# === Core ===
from datetime import timedelta
import random
import string
from pydantic import Field
from secrets import token_hex

# === Utils ===
from packages.backend.utils.exception.websocket import WebsocketException
from utils.helper.time import now, future
from utils.abc.handlers.user import User
from utils.abc.handlers._class import Class
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
    
    target_id: Optional[str] = None
    
    __collection__: ClassVar[Collection] = MongoClient.invites
    id: str = Field(default_factory=lambda: token_hex(32))
    
    def link(self, user: User) -> None:
        """
        Links a user to the target of this invite. Depending on what
        the type of the invite this is, the user will either be linked to a class or
        a parent
        
        :param User user: User that's going to be linked
        """
        
        if not user.is_student:
            raise WebsocketException(None, "You aren't a student")

        target = self.target
        
        if target is None:
            raise WebsocketException(None, message="No target was found when linking")

        if self.type == "class":
            if not isinstance(target, Class):
                raise WebsocketException(None, message="Expected a Class as target")
            
            if target.has_student(user.id):
                raise WebsocketException(None, message="You're already in the class")
            
            target.add_student(user.id)

        elif self.type == "parent":
            if not isinstance(target, User):
                raise WebsocketException(None, message="Expected a User as parent target")
            
            if user.id in (target.student_ids or []):
                raise WebsocketException(None, message="You're already linked to this parent")
            
            target.update(None, "$addToSet", {"student_ids": user.id})

        else:
            raise WebsocketException(None, message="Unmatched target type")

    @property
    def target(self) -> User | Class | None:
        """
        Attempts to get the target attached to this session
        
        :returns User | Class | None: If the user or class is found, otherwise None
        """

        if self.target_id is None:
            return None

        if self.type not in ["class", "parent"]:
            return None

        lookup = Class if self.type == "class" else User

        try:
            return lookup.get(id=self.target_id)
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