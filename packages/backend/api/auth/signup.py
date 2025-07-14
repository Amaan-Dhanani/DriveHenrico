from utils import app
from utils.console import console
from quart import websocket
from utils.helper.websocket import Websocket
from quart.ctx import has_websocket_context

blueprint = app.Blueprint("api:@signup", __name__)
_ws = Websocket()

async def ran_operation(*args, **kwargs):
    console.info("Hi there")
    return {"hi": "there"}

@blueprint.websocket("/auth/signup")
@_ws.init
@_ws.on("operation", callback=ran_operation)
async def signup_WS(*args, **kwargs):
    console.info("This shouldn't be called I don't think")
        
