# === Core ===
from dataclasses import dataclass

# === Utilities
from utils import websocket_auth, websocket_message
from utils.abc import Invite

# === Typing ===
from typing import Optional

# === Errors ===
from utils.exception.websocket import WebsocketException 

@dataclass
class D:
    email: Optional[str] = None

async def parent_create_invite(*_, **__):
    """
    Parent wants to create an invite
    
    :param Optional[str] email: Email of the student, if this is 
    present, also send an email to the student in question so long 
    as they're a registered student
    
    :raises WebsocketException:

        - If the user doesn't exist
        - If the user isn't a parent account
    """
    
    data: D = websocket_message.cast_data(D)
    
    user = websocket_auth.user
    
    if user is None:
        raise WebsocketException(operation="creation:failed", message="User isn't specified, did you auth?")
    
    if not user.is_parent:
        raise WebsocketException(operation="creation:failed", message="You are not a parent")
    
    invite = Invite.from_user(user)
    invite.insert()
    
    return "invite:created", {"invite_id": invite.id, "invite_code": invite.code}
    