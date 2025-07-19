# === Core ===


# === Utilities ===
from utils import app
from utils.console import console
from utils.helper.websocket import Websocket
from utils.abc.handlers.user import User
from utils.abc.handlers.credential import Credential
from utils.abc.handlers.verification import Verification
from utils.abc.handlers.session import Session


# === Type Hinting ===
from typing import TypedDict


blueprint = app.Blueprint("api:@signup", __name__)

class AuthSignupPostData(TypedDict):
    email: str
    password: str
    account_type: str

async def auth_signup_post(key: str, value: str, data: AuthSignupPostData):
     
    if User.email_exists(data["email"]):
        raise ValueError("Email already exists")
    
    # Insert New User
    new_user = User.create({"account_type": data["account_type"], "email": data["email"] }).insert()
    
    # Insert Credentials
    Credential.create(new_user, data["password"]).insert()
    
    # Insert Verification
    new_verification = Verification.create(new_user).insert()
    
    console.info(f"Sending email to {new_user.email}, code sent: {new_verification.code}")   
    
    return {"verification_id": new_verification.id}
    


class AuthSignupConfirmCodeData(TypedDict):
    id: str
    code: str


async def auth_signup_confirm_code(key: str, value: str, data: AuthSignupConfirmCodeData):
    
    if not Verification.exists(data["id"]):
        raise KeyError("Verification ID Doesn't exist")
    
    verification = Verification.get(data["id"])
    if verification.code != data["code"]:
        raise ValueError("Incorrect Code")
    
    if not User.exists(verification.account_id):
        raise LookupError(f"User with id {verification.account_id} does not exist.")
    
    user = User.get(verification.account_id) # Fails if not found
    user.update("$set", {"verified": True})
    
    new_session = Session.create(user).insert()
    verification.delete()
    
    return {"token": new_session.id}



_ws = Websocket()
@blueprint.websocket("/auth/signup")
@_ws.init
@_ws.on("operation", value="auth:signup:post", callback=auth_signup_post)
@_ws.on("operation", value="auth:signup:confirm_code", callback=auth_signup_confirm_code)
async def signup_WS(*args, **kwargs):
    console.info("This shouldn't be called I don't think")
        
