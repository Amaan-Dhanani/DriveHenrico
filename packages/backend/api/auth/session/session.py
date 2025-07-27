# === Core ===

# === Utilities ===
from utils import app
from utils.helper import websocket

# === Listeners ===
from ._initiate import initiate
from ._verify import verify

blueprint = app.Blueprint("api(auth):@session", __name__)


_ws = websocket.Websocket()
@blueprint.websocket("/auth/session")
@_ws.init
@_ws.on("operation", value="session:initiate", callback=initiate)
@_ws.on("operation", value="session:verify", callback=verify)
async def session_WS(*args, **kwargs):
    print("...?")