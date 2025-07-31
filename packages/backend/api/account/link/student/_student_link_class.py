# === Core ===
from dataclasses import dataclass

# === Utilities ===
from utils import websocket_auth, websocket_message
from utils.abc import Class

# === Errors ===
from utils.exception.websocket import WebsocketException 

@dataclass
class D:
    class_code: str

def student_link_class(*_, **__):
    """
    Operation is used whenever a student wants to link to a class
    
    :param str class_code: Code of the class
    
    :raises WebsocketException: 
    
        - If the user doesn't exist
        - If the user isn't a student account
        - If the class doesn't exist
        - If the user is already in the class
    """
    
    data: D = websocket_message.cast_data(D)
    
    user = websocket_auth.user
    
    if user is None:
        raise WebsocketException(operation="link:rejected", message="User isn't specified, did you auth?")
    
    if not user.is_student:
        raise WebsocketException(operation="link:rejected", message="You are not a student")
    
    try:        
        _class = Class.get(invite_code=data.class_code)        
    except LookupError:
        raise WebsocketException(operation="link:rejected", message=f"No class has the code {data.class_code}")
    
    if _class.has_user(user.id):
        raise WebsocketException(operation="link:rejected", message=f"Class already has user")
    
    if user.class_id is not None:
        raise WebsocketException(operation="link:rejected", message=f"User already in class")
    
    _class.add_user(user.id)
    
    return "link:established", {"class_id": _class.id}