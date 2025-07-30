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

from health import health
from auth import PARENT_TOKEN, STUDENT_TOKEN, auth_as, TEACHER_TOKEN
from used_json import *

# === Suite ===
import json
import httpx
import websockets

APP_DOMAIN = Yaml().get("app_domain")
API_DOMAIN = f"api.{APP_DOMAIN}"
WSS_ROUTE = f"wss://{API_DOMAIN}"
HTTPS_ROUTE = f"https://{API_DOMAIN}"


client = httpx.AsyncClient(verify=False)


APP_DOMAIN = Yaml().get("app_domain")
API_DOMAIN = f"api.{APP_DOMAIN}"
WSS_ROUTE = f"wss://{API_DOMAIN}"
HTTPS_ROUTE = f"https://{API_DOMAIN}"


async def main():
    await health(client, HTTPS_ROUTE)

    route_session = f"{WSS_ROUTE}/account/link"
    console.debug(f"Connecting to {route_session}")

    async with websockets.connect(route_session) as ws:
        await auth_as(ws, TEACHER_TOKEN)
        
        _payload_create_class = to_json({
            "operation": "teacher:create_class",
            "data": {
                "name": "Amazing Class"
            }
        })
        
        await ws.send(_payload_create_class)
        response = from_json(await ws.recv())
        
        print(response)


if __name__ == "__main__":
    asyncio.run(main())
