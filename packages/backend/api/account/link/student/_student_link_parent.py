# === Core ===
from dataclasses import dataclass

# === Utilities ===
from utils import websocket_auth, websocket_message
from utils.abc import Invite

# === Errors ===
from utils.exception.websocket import WebsocketException


@dataclass
class D:
    invite_code: str


async def student_link_parent(*_, **__):
    """
    Operation is used whenever a student wants to link to a class
    
    :param str invite_code: Invite code 
    
    :rases WebsocketException:
    
        - If the user doesn't exist
        - If the user isn't a student account
        - If the student already has a parent linked
        - If the invite doesn't exist
        - If the parent doesn't exist
        - if the student is already linked to the parent
                
    """

    data: D = websocket_message.cast_data(D)

    user = websocket_auth.user

    if user is None:
        raise WebsocketException(operation="link:rejected", message="User isn't specified, did you auth?")

    if not user.is_student:
        raise WebsocketException(operation="link:rejected", message="You are not a student")

    if user.parent_id is not None:
        raise WebsocketException(operation="link:rejected", message="You're already linked to a parent")

    try:
        invite = Invite.get(code=data.invite_code)
    except LookupError:
        raise WebsocketException(operation="link:rejected", message="Invite doesn't exist")

    if invite.parent is None:
        raise WebsocketException(operation="link:rejected", message="Parent of invite doesn't exist")

    if user.id in (invite.parent.class_ids or []):
        raise WebsocketException(operation="link:rejected", message="You're already linked to this parent")
    
    return "link:established", {}
