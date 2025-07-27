# === Core ===
from hashlib import sha512
from dataclasses import dataclass

# === Utilities ===
from utils import websocket_message
from utils.abc import User, Credential

# === Errors ===
from utils.exception.websocket import NotExistsError, WebsocketException

@dataclass
class D_InitiateRequest:
    method: str
    email: str
    password: str

async def initiate(*args, **kwargs):
    data: D_InitiateRequest = websocket_message.cast_data(D_InitiateRequest)
    
    try:
        user = User.get(email=data.email)
    except LookupError:
        raise NotExistsError(operation="session:rejected", identifier="user")
    
    try:
        credential = Credential.get(account_id=user.id)
    except LookupError:
        raise NotExistsError(operation="session:rejected", identifier="credential")
    
    salt = credential.salt
    check_hashed = sha512((data.password + salt).encode("utf-8")).hexdigest()
    
    if check_hashed != credential.hashed:
        raise WebsocketException(operation="session:rejected", message="Incorrect Password")
    
    
    return "session:challenge", {"challenge_id": ";;;;", "method": "code"}