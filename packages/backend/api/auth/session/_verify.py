# === Core ===
from dataclasses import dataclass

# === Utilities ===
from utils import websocket_message
from utils.abc import Challenge, Session

# === Errors ===
from utils.exception.websocket import NotExistsError, WebsocketException

@dataclass
class D_VerifyRequest:
    challenge_id: str
    value: str

async def verify(*args, **kwargs):
    data: D_VerifyRequest = websocket_message.cast_data(D_VerifyRequest)

    try:
        challenge = Challenge.get(challenge_id=data.challenge_id)
    except LookupError:
        raise NotExistsError(operation="session:rejected", identifier="challenge")
    
    user = challenge.user
    if not user:
        raise NotExistsError(operation="session:rejected", identifier="user")
    
    with challenge.attempt(data.value) as attempt:
        if not attempt.ok:
            
            if attempt.expired:
                raise WebsocketException(operation="session:rejected", message="Challenge Expired")
            
            if attempt.too_many_attempts:
                raise WebsocketException(operation="session:rejected", message="Too many attempts")
        
            if attempt.incorrect:
                raise WebsocketException(operation="session:rejected", message="Incorrect Input")

            raise WebsocketException(operation="session:rejected", message="Attempt not ok")  

        challenge.delete()
        
        if not user.verified:
            user.update({"id": user.id}, "$set", {"verified": True})
    
    session = Session.from_user(user).insert()
        
    return "session:established", {"token": session.id}