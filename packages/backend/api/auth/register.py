# === Core ===
from dataclasses import dataclass
from datetime import datetime, timezone

# === Utilities ===
from utils import app, websocket_message
from utils.console import console
from utils.helper.websocket import Websocket
from utils.abc import User, Credential, Verification, Session
from utils.exception.websocket import EmailExistsError, NotExistsError
from utils.mongo.Client import MongoClient
from utils.email import CodeEmail
from utils.app.Quart import app as _app


blueprint = app.Blueprint("api(auth):@register", __name__)


@dataclass
class D_AuthSignupPost:
    email: str
    name: str
    password: str
    account_type: str


async def auth_register_post(*_, **__):

    data: D_AuthSignupPost = websocket_message.cast_data(D_AuthSignupPost)

    if User.exists(email=data.email):
        raise EmailExistsError(data.email)

    user = User.create(**{
        "email": data.email,
        "name": data.name,
        "account_type": data.account_type
    }).insert()

    Credential.from_user(user, data.password).insert()

    verification = Verification.from_user(user).insert()

    await CodeEmail(to=user.email, code=verification.code).send()

    console.info(f"Sending email to {user.email}, code sent: {verification.code}")

    return {"verification_id": verification.id}


@dataclass
class D_AuthSignupConfirmCode:
    id: str
    code: str


async def auth_register_confirm_code(*_, **__):
    data: D_AuthSignupConfirmCode = websocket_message.cast_data(D_AuthSignupConfirmCode)

    if not Verification.exists(id=data.id):
        raise NotExistsError("Verification ID", data.id)

    verification = Verification.get(id=data.id)
    if verification.code != data.code:
        raise ValueError("Incorrect Code")

    user = User.get(id=verification.account_id)
    user.set({"verified": True, "ttl": None})

    session = Session.from_user(user).insert()
    verification.delete()

    return {"token": session.id}


_ws = Websocket()


@blueprint.websocket("/auth/register")
@_ws.init
@_ws.on("operation", value="auth:register:post", callback=auth_register_post)
@_ws.on("operation", value="auth:register:confirm_code", callback=auth_register_confirm_code)
async def register_WS(*args, **kwargs):
    console.info("This shouldn't be called I don't think")


@_app.register_task("unverified_cleanup", minutes=10)
async def unverified_cleanup():
    result = MongoClient.users.delete_many({
        "verified": False,
        "ttl": {"$lt": int(datetime.now(timezone.utc).timestamp())}
    })

    if result.deleted_count > 0:
        console.info(f"Unverified Cleanup Deleted {result.deleted_count} Accounts")
