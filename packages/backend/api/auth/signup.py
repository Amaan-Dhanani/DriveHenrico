from utils import app
from utils.console import console
from quart import websocket

blueprint = app.Blueprint("api:@signup", __name__)

@blueprint.websocket("/auth/signup")
async def signup_WS(*args, **kwargs):
    console.info("WS Connection", log_locals=True)
    
    while True:
        recv = await websocket.receive()
        console.debug("Received", recv)
        
        console.debug("Sending", recv)
        await websocket.send(recv)
        
