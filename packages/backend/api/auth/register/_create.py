# === Core ===
from hashlib import sha512
from dataclasses import dataclass

# === Utilities ===
from utils import websocket_message
from utils.abc import User, Credential

# === Errors ===
from utils.exception.websocket import WebsocketException 

@dataclass
class D_AuthSignupPost:
    email: str
    name: str
    password: str
    account_type: str

async def create(*_, **__):
    """
    This handler should only create the user, 
    create the credentials for the user
    and return some success message.
    
    :param str email: New user email
    :param str name: User full name
    :param str password: User password
    :param str account_type: User account type
    
    :raises WebsocketException: If the user email already exists within the database
    """

    data: D_AuthSignupPost = websocket_message.cast_data(D_AuthSignupPost)

    if User.exists(email=data.email):
        raise WebsocketException(operation="register:rejected", message="Email already exists")

    user = User.create(**{
        "email": data.email,
        "name": data.name,
        "account_type": data.account_type
    }).insert()

    Credential.from_user(user, data.password).insert()

    return "register:success", {"user_id": user.id}
