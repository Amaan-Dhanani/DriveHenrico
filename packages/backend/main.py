
import sys
sys.dont_write_bytecode = True

import uvicorn
from utils.app.Quart import app
from siblink import Config


# Load Everything
Config.gather_predetermined()
app.register_blueprints()

uvicorn.run(app, **app.uvicorn_config)

