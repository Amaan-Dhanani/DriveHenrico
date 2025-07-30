# === Core ===
from dataclasses import dataclass

# === Utilities ===
from utils import websocket_auth, websocket_message
from utils.abc import Class

# === Errors ===
from utils.exception.websocket import WebsocketException 

@dataclass
class D:
    name: str

async def teacher_create_class(*_, **__):
    """
    This operation is used whenever a teacher wants to create a class
    
    :param str name: Name of the class
    
    :raises WebsocketException: If the user doesn't exist or the user isn't a teacher
    """
    
    data: D = websocket_message.cast_data(D)
    
    user = websocket_auth.user
    
    if user is None:
        raise WebsocketException(operation="creation:unsuccessful", message="User isn't specified")
    
    if not user.is_teacher:
        raise WebsocketException(operation="creation:unsuccessful", message="You aren't a teacher")
    
    _class = Class.from_user(user, name=data.name)
    _class.insert()
    
    return "class:created", {"class_id": _class.id}
    