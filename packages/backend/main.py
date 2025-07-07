import uvicorn

from quart import Quart

app = Quart(__name__)

uvicorn.run(app)