from quart import Response
from utils import app

blueprint = app.Blueprint("api:@health", __name__)

@blueprint.route(rule="/health", methods=["GET"])
async def health_GET(*args, **kwargs):
    return Response(status=200)