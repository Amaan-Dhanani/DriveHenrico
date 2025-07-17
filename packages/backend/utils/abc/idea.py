# === Core ===
from dataclasses import asdict
import hashlib
import secrets

# === Utilities ===
from utils import app
from utils.console import console
from utils.helper.websocket import Websocket
from utils.mongo.Client import MongoClient
from utils.mongo.abc import users_collection, verification_collection, credentials_collection

from utils.types.user import User
from utils.types.verification import Verification
from utils.types.credentials import Credentials

# === Type Hinting ===
from typing import TypedDict


blueprint = app.Blueprint("api:@signup", __name__)

class AuthSignupPostData(TypedDict):
    email: str
    password: str
    account_type: str

async def auth_signup_post(key: str, value: str, data: AuthSignupPostData):
    
    # For now assume email, password, and account_type are valid
    user = User(email=data.email)
    
    if user.exists:
        return UserExists(email=data.email)
    
    user = User.create(email=data.email, account_type=data.account_type)
    Credentials.create(user, password=data.password)
    
    # Has hashed, and salt, and account_id
    
    verification = Verification.create(user)

    # send email
    console.info(f"Sending email to {user.email}, code sent: {verification.code}")    
    
    return {"operation": "auth:signup:await_code", "data": {"verification_id": verification._id}}


class AuthSignupConfirmCodeData(TypedDict):
    id: str
    code: str


async def auth_signup_confirm_code(key: str, value: str, data: AuthSignupConfirmCodeData):
    
    verification = Verification(data.id)
    user = User(verification.id)
    
    if not verification.exists:
        raise VerificationNotFound(id=data.id)
    
    if not verification.code == data.code:
        raise VerificationCodeIncorrect(data.code)
    
    if not user.exists:
        raise UserNotFound(id=data.id)
    
    user.set("verified", True)
    verification.delete()
    
    session = Session.create(account_id=user._id)
    
    return ok(session, "token")    
    

_ws = Websocket()
@blueprint.websocket("/auth/signup")
@_ws.init
@_ws.on("operation", value="auth:signup:post", callback=auth_signup_post)
@_ws.on("operation", value="auth:signup:confirm_code", callback=auth_signup_confirm_code)
async def signup_WS(*args, **kwargs):
    console.info("This shouldn't be called I don't think")
        
