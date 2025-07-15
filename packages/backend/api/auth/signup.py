# === Core ===
import hashlib
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


async def auth_signup_confirm_code(*args, **kwargs):
    console.info("auth:signup:confirm_code", log_locals=True)
    return {"hello":  "again"}


_ws = Websocket()
@blueprint.websocket("/auth/signup")
@_ws.init
@_ws.on("operation", value="auth:signup:post", callback=auth_signup_post)
@_ws.on("operation", value="auth:signup:confirm_code", callback=auth_signup_confirm_code)
async def signup_WS(*args, **kwargs):
    console.info("This shouldn't be called I don't think")
        
