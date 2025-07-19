# === Utilities ===
from dataclasses import dataclass
from utils import app, websocket_message
from utils.console import console
from utils.helper.websocket import Websocket
from utils.abc import User, Credential, Verification, Session
from utils.exception.websocket import EmailExistsError, NotExistsError



blueprint = app.Blueprint("api:@signup", __name__)


@dataclass
class D_AuthSignupPost:
    email: str
    password: str
    account_type: str


async def auth_signup_post(*_, **__):

    data: D_AuthSignupPost = websocket_message.cast_data(D_AuthSignupPost)

    if User.exists(email=data.email):
        raise EmailExistsError(data.email)

    user = User.create(**{
        "email": data.email,
        "account_type": data.account_type
    }).insert()

    Credential.from_user(user, data.password).insert()

    verification = Verification.from_user(user).insert()

    console.info(f"Sending email to {user.email}, code sent: {verification.code}")

    return {"verification_id": verification.id}


@dataclass
class D_AuthSignupConfirmCode:
    id: str
    code: str


async def auth_signup_confirm_code(*_, **__):
    data: D_AuthSignupConfirmCode = websocket_message.cast_data(D_AuthSignupConfirmCode)

    if not Verification.exists(id=data.id):
        raise NotExistsError("Verification ID", data.id)

    verification = Verification.get(id=data.id)
    if verification.code != data.code:
        raise ValueError("Incorrect Code")

    user = User.get(id=verification.account_id)
    user.set({"verified": True})

    session = Session.from_user(user).insert()
    verification.delete()

    return {"token": session.id}


_ws = Websocket()


@blueprint.websocket("/auth/signup")
@_ws.init
@_ws.on("operation", value="auth:signup:post", callback=auth_signup_post)
@_ws.on("operation", value="auth:signup:confirm_code", callback=auth_signup_confirm_code)
async def signup_WS(*args, **kwargs):
    console.info("This shouldn't be called I don't think")
