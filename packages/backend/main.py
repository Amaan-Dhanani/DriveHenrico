from asyncio import sleep
import sys
from typing import Any, Dict
sys.dont_write_bytecode = True

import uvicorn

from siblink import Config
Config.gather_predetermined()  # Gather base config vars immediately

from utils.console import console
from utils.app.Quart import app
from utils.helper.config import Yaml
from quart import request

# Ensure Config
try:
    Yaml()
except FileNotFoundError:
    print("Failed to run, no config file specified was found.\n You should copy config.example.yml into config.yml and try again.")
    quit()


# Load Everything
app.register_blueprints()


@app.before_serving
async def startup_log():
    yml = Yaml()
    uvicorn_config = yml.get("backend.uvicorn_config")

    console.info(f"Status : [green]Active[/]")
    console.info(f"IP     : http://{uvicorn_config['host']}:{uvicorn_config['port']}")
    console.info(f"Domain : https://api.{yml.get('app_domain')}")


@app.after_request
async def after_request(response):
    ip = request.remote_addr or "unknown"
    method = request.method
    path = request.path
    status = response.status_code

    console.info(f'{ip} - "{method} {path}" - {status}')
    return response


console.info("Waiting for application startup")

yml = Yaml()
raw = yml.get("backend.uvicorn_config")
populated: Dict[str, Any] = yml.populate_environment(raw)
uvicorn.run(app, **populated)
