# === Core ===
from dataclasses import dataclass

# === Utilities ===
from utils import websocket_auth, websocket_message
from utils.abc import Class

# === Errors ===
from utils.exception.websocket import WebsocketException 

@dataclass
class D:
    class_id: str

def teacher_regenerate_code(*_, **__):
    """
    Operation is used whenever a teacher wants to refresh a classes code
    
    :param str class_id: ID of the class
    
    :raises WebsocketException: 
    
        - If the user doesn't exist
        - If the user isn't a teacher account
        - If the class doesn't exist
    """
    
    data: D = websocket_message.cast_data(D)
    
    user = websocket_auth.user
    
    if user is None:
        raise WebsocketException(operation="regenerate:rejected", message="User isn't specified, did you auth?")
    
    if not user.is_teacher:
        raise WebsocketException(operation="regenerate:rejected", message="You are not a teacher")
    
    try:        
        _class = Class.get(id=data.class_id)        
    except LookupError:
        raise WebsocketException(operation="regenerate:rejected", message="Class wasn't found")
    
    _class.refresh_invite_code()
    
    return "link:established", {"class_code": _class.invite_code}