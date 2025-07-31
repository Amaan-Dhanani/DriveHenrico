# === Utilities ===
from utils import app
from utils.helper.websocket import Websocket

# === Listeners ===
from .teacher import teacher_create_class, teacher_regenerate_code
from .student import student_link_class

blueprint = app.Blueprint("api(account):@link", __name__)
_ws = Websocket()

@blueprint.websocket("/account/link")
@_ws.init
@_ws.auth(global_auth=True)
@_ws.on("operation", value="teacher:create_class", callback=teacher_create_class)
@_ws.on("operation", value="teacher:regenerate_code", callback=teacher_regenerate_code)
@_ws.on("operation", value="student:link_class", callback=student_link_class)
async def account_link(*_, **__):
    pass