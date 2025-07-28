# === Core ===
from datetime import datetime, timezone

# === Utilities ===
from utils import app
from utils.console import console
from utils.helper.websocket import Websocket
from utils.mongo.Client import MongoClient
from utils.app.Quart import app as _app

# === Listeners ===
from ._create import create

blueprint = app.Blueprint("api(auth):@register", __name__)
_ws = Websocket()

@blueprint.websocket("/auth/register")
@_ws.init
@_ws.on("operation", value="register:create", callback=create)
async def register_WS(*args, **kwargs):
    print("")

@_app.register_task("unverified_cleanup", minutes=10)
async def unverified_cleanup():
    result = MongoClient.users.delete_many({
        "verified": False,
        "ttl": {"$lt": int(datetime.now(timezone.utc).timestamp())}
    })
    if result.deleted_count > 0:
        console.info(f"Unverified Cleanup Deleted {result.deleted_count} Accounts")
