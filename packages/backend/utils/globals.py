from utils.app.Quart import app

from contextvars import ContextVar
from typing import TYPE_CHECKING

from werkzeug.local import LocalProxy

if TYPE_CHECKING:
    from .ctx import WebsocketMessageContext
    from .ctx import WebsocketAuthContext


_no_websocket_context_msg = "Not within a websocket message context"
_cv_websocket_message: ContextVar["WebsocketMessageContext"] = ContextVar("backend.websocket_message")
websocket_message: "WebsocketMessageContext" = LocalProxy(
    _cv_websocket_message, unbound_message = _no_websocket_context_msg
)

_no_websocket_auth_context_msg = "Not within a websocket auth context"
_cv_websocket_auth: ContextVar["WebsocketAuthContext"] = ContextVar("backend.websocket_auth")
websocket_auth: "WebsocketAuthContext" = LocalProxy(
    _cv_websocket_auth, unbound_message=_no_websocket_auth_context_msg
)