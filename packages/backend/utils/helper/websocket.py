# === Core ===
import asyncio
from quart import websocket

# === Utilities ===
from utils import _cv_websocket_message

from utils.console import console
from utils.ctx import WebsocketMessageContext
from utils.exception.websocket import WebsocketException

# === Type Hinting ===
from typing import Any, Awaitable, Callable, List, Optional
from dataclasses import dataclass

# === Errors ===
import json
from json.decoder import JSONDecodeError

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


class Websocket:
    """
    Websocket namespace, used for websocket handling for
    easy development. A lot of abstraction here so keep an eye out.
    """

    def __init__(self) -> None:
        self.listeners: List[Listener] = []

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
            await asyncio.gather(self.__reader(), func(*args, **kwargs))
            return
        return decorator

    def on(self, key: str, value: Optional[Any] = _SENTINEL, *, callback: Callable):
        """
        Registers a websocket listener for the websocket request. Only reads valid json messages.

        If no `value` is specified, only listen for `key`

        :param str key: Key of the json request to be checked
        :param Optional[Any] value: Value that the key should be in order for the callback to fire
        :param Callable callback: Callback function that is ran whenever the key and value match
        """

        # Register the listener
        self.listeners.append(Listener(key=key, value=value, callback=callback))

        def wrapper(func: Callable):
            async def decorator(*args, **kwargs):
                # Continue to run decorated function
                return await func(*args, **kwargs)
            return decorator
        return wrapper
