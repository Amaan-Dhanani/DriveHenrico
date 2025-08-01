# === Core ===
from dataclasses import dataclass

# === Utilities ===
from utils import websocket_auth, websocket_message
from utils.abc import Invite

# === Typing ===
from typing import Literal

# === Errors ===
from utils.exception.websocket import WebsocketException

@dataclass
class D:
    type: Literal["class", "parent"]

async def student_unlink(*_, **__):
    """
    Operation is used whenever a student wants to unlink from
    either a parent or a class
    
    :param str type: Type of unlink
    
    :raises WebsocketException:

        - If the type isn't valid (not class or parent)
        - If the user doesn't exist
        - If the user isn't a student account
        - If the student doesn't have the `type` linked
    """
    
    data: D = websocket_message.cast_data(D)

    user = websocket_auth.user
    
    if data.type not in ["class", "parent"]:
        raise WebsocketException(operation="unlink:rejected", message="Type isn't valid")

    if user is None:
        raise WebsocketException(operation="unlink:rejected", message="User isn't specified, did you auth?")

    if not user.is_student:
        raise WebsocketException(operation="unlink:rejected", message="You are not a student")

    if data.type == "class":
        if user.class_id is None:
            raise WebsocketException(operation="unlink:rejected", message="No class to unlink")
    
    if data.type == "parent":
        if user.parent_id is None:
            raise WebsocketException(operation="unlink:rejected", message="No parent to link")
    
    return "unlink:successful", {}