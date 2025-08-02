# === Utilities ===
from utils import app
from utils.helper.websocket import Websocket

# === Listeners ===
from .teacher import teacher_create_class, teacher_regenerate_code
from .student import student_link, student_unlink
from .parent import parent_create_invite, parent_revoke_invite

blueprint = app.Blueprint("api(account):@link", __name__)
_ws = Websocket()

@blueprint.websocket("/account/link")
@_ws.init
@_ws.auth(global_auth=True)
@_ws.on("operation", value="teacher:create_class", callback=teacher_create_class)
@_ws.on("operation", value="teacher:regenerate_code", callback=teacher_regenerate_code)
@_ws.on("operation", value="student:link", callback=student_link)
@_ws.on("operation", value="student:unlink", callback=student_unlink)
@_ws.on("operation", value="parent:create_invite", callback=parent_create_invite)
@_ws.on("operation", value="parent:revoke_invite", callback=parent_revoke_invite)
async def account_link(*_, **__):
    pass