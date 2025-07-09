
import sys
sys.dont_write_bytecode = True

import uvicorn
from utils.app.Quart import app

# Load Everything
app.register_blueprints()

uvicorn.run(app, **app.uvicorn_config)

