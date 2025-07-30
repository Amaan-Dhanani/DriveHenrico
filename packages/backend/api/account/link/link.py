# === Utilities ===
from utils import app
from utils.helper.websocket import Websocket

# === Listeners ===
from .teacher import teacher_create_class

blueprint = app.Blueprint("api(account):@link", __name__)
_ws = Websocket()

@blueprint.websocket("/account/link")
@_ws.init
@_ws.auth(global_auth=True)
@_ws.on("operation", value="teacher:create_class", callback=teacher_create_class)
async def account_link(*_, **__):
    pass