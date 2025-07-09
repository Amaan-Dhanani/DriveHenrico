from utils import app

blueprint = app.Blueprint("api:@ping", __name__)

@blueprint.route(rule="/ping", methods=["GET"])
async def ping_GET(*args, **kwargs):
    print("Get")
    return {
        "pong": True
    }