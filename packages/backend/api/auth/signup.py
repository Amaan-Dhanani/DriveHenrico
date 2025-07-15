# === Core ===
import hashlib
from operator import truediv
import secrets
import random

# === Utilities ===
from utils import app
from utils.console import console
from utils.helper.websocket import Websocket
from utils.mongo.Client import MongoClient

# === Type Hinting ===
from typing import TypedDict

blueprint = app.Blueprint("api:@signup", __name__)

class AuthSignupPostData(TypedDict):
    email: str
    password: str
    account_type: str

async def auth_signup_post(key: str, value: str, data: AuthSignupPostData):
    
    # For now assume email, password, and account_type are valid
    
    # Check if email already exists
    search_user = MongoClient.users.find_one({"email": data["email"]})
    if search_user:
        return {"operation": value, "error": "An account with this email already exists"}
    
    # Generate Salt & Hash
    salt = secrets.token_hex(32)
    hashed = hashlib.sha512((data["password"] + salt).encode("utf-8")).hexdigest()
    id = "user_{}".format(secrets.token_hex(32))
    
    # Save Credentials
    MongoClient.credentials.insert_one({
        "email": data["email"],
        "hashed": hashed,
        "salt": salt,
        "_id": id
    })
    
    # Push user to database
    MongoClient.users.insert_one({
        "email": data["email"],
        "account_type": data["account_type"],
        "verified": False,
        "_id": id
    })
    
    # create verification id and code pair
    verification_id = "verification_{}".format(secrets.token_hex(64))
    verification_code = "".join(random.choices('0123456789', k=6))
    
    # push verification_id and code to database
    MongoClient.verification.insert_one({
        "account_id": id,
        "code": verification_code,
        "_id": verification_id
    })
    
    # send email
    console.info("Sending email to {}, code sent: {}".format(data["email"], verification_code))    
    
    return {"operation": "auth:signup:await_code", "data": {"verification_id": verification_id}}


class AuthSignupConfirmCodeData(TypedDict):
    id: str
    code: str


async def auth_signup_confirm_code(key: str, value: str, data: AuthSignupConfirmCodeData):
    
    VerificationSearch = MongoClient.verification.find_one({"_id": data["id"]})
    if not VerificationSearch:
        return {"operation": value, "error": "Verification ID not found"}
    
    if VerificationSearch["code"] != data["code"]:
        return {"operation": value, "error": "Incorrect Code"}
    
    UserSearch = MongoClient.users.find_one({"_id": VerificationSearch["account_id"]})
    if not UserSearch:
        return {"operation": value, "error": "User object not found"}    
    
    # Make account verified
    MongoClient.users.update_one({"_id": VerificationSearch["account_id"]}, {"$set": {"verified": True}})
    
    # Delete Verification Id
    MongoClient.verification.delete_one({"_id": data["id"]})
    
    # Create Session Token
    token = "session_{}".format(secrets.token_hex(32))
    MongoClient.sessions.insert_one({"_id": token, "account_id": VerificationSearch["account_id"], "expires": None})
    
    # return session token    
    return {"operation": value, "data": {"token": token}}


_ws = Websocket()
@blueprint.websocket("/auth/signup")
@_ws.init
@_ws.on("operation", value="auth:signup:post", callback=auth_signup_post)
@_ws.on("operation", value="auth:signup:confirm_code", callback=auth_signup_confirm_code)
async def signup_WS(*args, **kwargs):
    console.info("This shouldn't be called I don't think")
        
