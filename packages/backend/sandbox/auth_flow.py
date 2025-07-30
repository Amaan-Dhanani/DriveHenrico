import http
import sys
sys.dont_write_bytecode = True

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import asyncio

# === Inner Library ===
from siblink import Config
Config.gather_predetermined()

from utils.helper.config import Yaml
from utils.console import console

# === Suite ===
import json
import httpx
import websockets

APP_DOMAIN = Yaml().get("app_domain")
API_DOMAIN = f"api.{APP_DOMAIN}"
WSS_ROUTE = f"wss://{API_DOMAIN}"
HTTPS_ROUTE = f"https://{API_DOMAIN}"


client = httpx.AsyncClient(verify=False)


async def health():
    route_health = f"{HTTPS_ROUTE}/health"
    console.log(f"Health Check {route_health}")
    for _ in range(30):
        try:
            response = await client.get(route_health)
            console.debug(response)
            if response.status_code == 200:
                return
        except Exception as e:
            pass
        console.log("Waiting...")
        await asyncio.sleep(1)
    raise RuntimeError("Backend didn't run in time")


def to_json(data: dict) -> str:
    return json.dumps(data)


def from_json(data: str) -> dict:
    return json.loads(data)

async def authenticate(websocket: websockets.ClientConnection, token: str) -> None:

    _payload_token = to_json({
        "operation": "auth:token",
        "data": {
            "token": token
        }
    })
    
    await websocket.send(_payload_token)
    
    response = from_json(await websocket.recv())
    
    if response["operation"] != "auth:success":
        print(response)
        quit()
        
    console.debug("Authenticated")


async def main():
    await health()

    route_session = f"{WSS_ROUTE}/account/link"
    console.debug(f"Connecting to {route_session}")

    async with websockets.connect(route_session) as ws:
        TOKEN = "03af3b1eb8f3e926a131832cd714f1e6b112f5440d1d9e43cea14c6d42722f91"
        await authenticate(ws, TOKEN)
        
        _payload_link = to_json({
            "operation": "foo:test",
            "data": {
                "heheheha": True
            }
        })
        
        await ws.send(_payload_link)
        
        response = await ws.recv()
        
        console.debug(response)
        
        

        
if __name__ == "__main__":
    asyncio.run(main())
