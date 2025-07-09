from time import sleep
import uvicorn
from quart import Quart

from utils.helper.config import Yaml

# app = Quart(__name__)

# uvicorn.run(app, **{"port": 4000, "host": "0.0.0.0"})

print(Yaml().parse())