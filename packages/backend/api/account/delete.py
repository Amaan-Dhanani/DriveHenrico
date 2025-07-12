from utils import app

blueprint = app.Blueprint("api:@account#delete", __name__)

@blueprint.route(rule="/account/delete", methods=["POST"])
async def delete_POST(*args, **kwargs):
    print("")