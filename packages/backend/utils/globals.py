from utils.app.Quart import app

from contextvars import ContextVar
from typing import TYPE_CHECKING

from werkzeug.local import LocalProxy

if TYPE_CHECKING:
    from .ctx import WebsocketMessageContext


_no_websocket_context_msg = "Not within a websocket message context"
_cv_websocket_message: ContextVar["WebsocketMessageContext"] = ContextVar("backend.websocket_message")
websocket_message: "WebsocketMessageContext" = LocalProxy(
    _cv_websocket_message, unbound_message = _no_websocket_context_msg
)