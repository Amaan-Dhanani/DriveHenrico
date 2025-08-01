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
    invite_id: str
    
async def parent_revoke_invite(*_, **__):
    """
    Parent wants to revoke an invite
    
    :param str invite_id: Id of the email to remove
    
    :raises WebsocketException:
        
        - If the user doesn't exist
        - If the user isn't a parent account
        - If the invite doesn't exist
        - If the parent didn't create the invite
    """
    
    data: D = websocket_message.cast_data(D)
    
    user = websocket_auth.user
    
    if user is None:
        raise WebsocketException(operation="revoke:rejected", message="User isn't specified, did you auth?")
    
    if not user.is_parent:
        raise WebsocketException(operation="revoke:rejected", message="You are not a parent")
    
    try:
        invite = Invite.get(id=data.invite_id)
    except LookupError:
        raise WebsocketException(operation="revoke:rejected", message="Invite doesn't exist")
    
    if invite.created_by != user.id:
        raise WebsocketException(operation="revoke:rejected", message="You didn't make this invite")
    
    invite.delete()
    
    return "revoke:success", {"invite_id": invite.id}