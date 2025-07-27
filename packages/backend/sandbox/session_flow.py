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


async def main():
    await health()

    route_session = f"{WSS_ROUTE}/auth/session"
    console.debug(f"Connecting to {route_session}")
    
    async with websockets.connect(route_session) as ws:
        
        _payload_initiate = to_json({
            "operation": "session:initiate",
            "data": {
                "method": "password",
                "email": "treltasev@gmail.com",
                "password": "1234"
            }
        })
        
        await ws.send(_payload_initiate)
       
        response = from_json(await ws.recv())

        console.debug(response)
    

if __name__ == "__main__":
    asyncio.run(main())

