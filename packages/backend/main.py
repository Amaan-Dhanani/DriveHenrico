import uvicorn

from quart import Quart

app = Quart(__name__)

uvicorn.run(app, **{"port": 4000, "host": "0.0.0.0"})