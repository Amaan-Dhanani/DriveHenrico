# === Core ===
import asyncio
from quart import websocket

# === Utilities ===
from utils import _cv_websocket_message, websocket_message
from utils import _cv_websocket_auth, websocket_auth

from utils.console import console
from utils.ctx import WebsocketAuthContext, WebsocketMessageContext
from utils.exception.websocket import WebsocketException
from utils.abc import Session

# === Type Hinting ===
from typing import Any, Awaitable, Callable, List, Optional
from dataclasses import dataclass

# === Errors ===
import json
from json.decoder import JSONDecodeError
from utils.exception.websocket import WebsocketException

_SENTINEL = object()


@dataclass(frozen=True, kw_only=True)
class Listener:
    """
    Strongly typed listener object

    :property str key: Key that the listener looks for
    :property Optional[Any] value: Value that the key should match, if no value is specified, if key is found, the callback is ran
    :property Callable callback: Callback function that is ran whenever the key and values match
    """
    key: str
    value: Any = _SENTINEL
    callback: Callable[..., Any]
    auth_required: bool
    ignore_auth: bool


class Websocket:
    """
    Websocket namespace, used for websocket handling for
    easy development. A lot of abstraction here so keep an eye out.
    """

    def __init__(self) -> None:
        self.listeners: List[Listener] = []
        self.global_auth: bool = False

    @staticmethod
    def looper(func: Callable[..., Awaitable[Any]]):
        async def decorator(self, *args, **kwargs):
            while True:
                try:
                    await func(self, *args, **kwargs)
                except Exception as e:
                    console.error("Loop Failed", e)
                    console.print_exception(show_locals=True)
        return decorator

    @looper
    async def __reader(self):
        """
        Continuous reader, matches the data with registered listeners
        in order to determine what function should be ran given a single request
        """

        # Parse request make sure its a dictionary
        try:
            json_request = json.loads(await websocket.receive())

            if not isinstance(json_request, dict):
                raise TypeError("Request when parsed isn't dict")

        except JSONDecodeError:
            console.error("Input received not json serializable")
            return

        except TypeError as e:
            console.error(e)
            return

        for listener in self.listeners:
            if not listener.key in json_request:
                continue

            # Skip if key doesn't equal value and listener value isn't sentinel
            if not json_request[listener.key] == listener.value and listener.value != _SENTINEL:
                continue
            
            
            # Update Current Message Context
            _cv_websocket_message.set(WebsocketMessageContext(
                operation=listener.value,
                data=json_request.get("data", None)
            ))       

            try:
                
                # Fail if authentication is at all required
                if not listener.ignore_auth:                    
                    if (self.global_auth or listener.auth_required) and not websocket_auth.authenticated:
                        raise WebsocketException(operation="auth:failed", message="Authentication is required", data={"on": websocket_message.operation})

                callback_response = await listener.callback()
                
                # If callback_response is a tuple, overwrite operation and data
                if isinstance(callback_response, tuple) and len(callback_response) == 2:
                    operation, data = callback_response
                    response = {
                        "operation": operation,
                        "data": data
                    }
                else:
                    response = {
                        "operation": listener.value,
                        "data": callback_response
                    }
                    
                await websocket.send_json(response)
            
            except WebsocketException as e:
                if e.kill:
                    await websocket.close(100)
                else:
                    console.print_exception()
                    await websocket.send_json(e.json)
            
            except Exception as e:
                console.info(e.__class__.__dict__)
                error = WebsocketException(
                    message=f"Unregistered Error {e.__class__.__name__}: {e}"
                )
                console.print_exception()
                await websocket.send_json(error.json)                
            
            

    def init(self, func: Callable):
        """
        Initializes the websocket handler by creating the reader task

        :param Callable func: The function to be called.
        """

        async def decorator(*args, **kwargs):
            
            _cv_websocket_auth.set(WebsocketAuthContext(
                None, self.global_auth
            ))
            
            await asyncio.gather(self.__reader(), func(*args, **kwargs))
            return
        return decorator

    def on(self, key: str, value: Optional[Any] = _SENTINEL, *, callback: Callable, auth_required: bool = False, ignore_auth: bool = False):
        """
        Registers a websocket listener for the websocket request. Only reads valid json messages.

        If no `value` is specified, only listen for `key`

        :param str key: Key of the json request to be checked
        :param Optional[Any] value: Value that the key should be in order for the callback to fire
        :param Callable callback: Callback function that is ran whenever the key and value match
        """

        # Register the listener
        self.listeners.append(Listener(key=key, value=value, callback=callback, auth_required=auth_required, ignore_auth=ignore_auth))

        def wrapper(func: Callable):
            async def decorator(*args, **kwargs):
                # Continue to run decorated function
                return await func(*args, **kwargs)
            return decorator
        return wrapper
    
    def auth(self, _func: Optional[Callable] = None, global_auth: bool = False):
        """
        Decorator used to enforce authentication 
        before any request is made. When this decorator is present on an endpoint
        
        :param Optional[Callable] _func: Decorated function (None)
        :param bool global_auth: if all callbacks are defaulted to require authentication (False)

        Usage
        -----
        ```python
        
        from utils import websocket_auth
        
        # Authentication not guaranteed
        def foo(*_, **__):
            websocket_auth.user # Either User or None
        
        # Authentication Required
        def buz(*_, *__):
            websocket_auth.user # Always User
            
        @_ws.init
        @_ws.auth
        @_ws.on("operation", value="some:operation", callback=foo)
        @_ws.on("operation", value="other:operation", callback=buz, auth_required=True)
        async def bar(*_, *__):
            pass            
        ```
        """

        @dataclass
        class D_AuthToken:
            token: str

        async def _auth_token(*_, **__):
            """
            Sets up the authentication context
            
            :param str token: User token
            
            :raises WebsocketException: If the token is invalid
            """
            data: D_AuthToken = websocket_message.cast_data(D_AuthToken)

            try:
                session = Session.get(id=data.token)
            except LookupError:
                raise WebsocketException(operation="auth:failed", message="Invalid Token")

            user = session.user
            if not user:
                raise WebsocketException(operation="auth:failed", message="User doesn't exist (this shouldn't happen)")

            _cv_websocket_auth.set(WebsocketAuthContext(
                user, global_auth
            ))
            
            return "auth:success", None

        # Register auth:token listener
        self.on("operation", value="auth:token", callback=_auth_token, ignore_auth=True)
        
        self.global_auth = True if global_auth else self.global_auth

        def wrapper(func: Callable):
            async def decorator(*args, **kwargs):
                # Continue to run the decorated function
                return await func(*args, **kwargs)
            return decorator

        if callable(_func):
            return wrapper(_func)

        return wrapper
