
import sys
sys.dont_write_bytecode = True

import uvicorn
from utils.app.Quart import app
from siblink import Config
from utils.helper.config import Yaml


# Ensure Config
try:
    Yaml()
except FileNotFoundError:
    print("Failed to run, no config file specified was found.\n You should copy config.example.yml into config.yml and try again.")
    quit()


# Load Everything
Config.gather_predetermined()
app.register_blueprints()

uvicorn.run(app, **Yaml().get("backend.uvicorn_config"))