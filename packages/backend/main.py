
import sys
sys.dont_write_bytecode = True

import uvicorn
from utils.app.Quart import app

uvicorn.run(app, **app.uvicorn_config)

