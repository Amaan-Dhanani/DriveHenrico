from typing import Any, Dict, List, Optional, Type
from utils import websocket_message


class WebsocketException(Exception):
    """
    Base class for exceptions raised during WebSocket communication.

    Attributes
    ----------
    operation : Optional[str]
        WebSocket operation name where the error occurred. Defaults to `websocket_message.operation` or "unspecified".
    message : Optional[str]
        Human-readable error message.
    data : Optional[dict[str, Any]]
        Optional structured payload to send to the client along with the error.
    kill : bool
        Whether to close the WebSocket connection after the error is sent.
    """

    def __init__(
        self,
        operation: Optional[str] = None,
        message: Optional[str] = None,
        data: Optional[Dict[str, Any]] = None,
        kill: bool = False,
        *args,
        **kwargs
    ):
        self.operation = operation or websocket_message.operation or "unspecified"
        self.message = message
        self.data = data
        self.kill = kill

        self.__dict__.update(kwargs)
        super().__init__(self.__str__(), *args)

    @property
    def json(self) -> Dict[str, Any]:
        """
        Returns a JSON-serializable dictionary representation of the error.
        """
        payload = {
            "operation": self.operation,
            "error": self.message,
        }

        if self.data is not None:
            payload["data"] = self.data

        return payload

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the exception.
        """
        return "/".join([
            "Websocket Exception Occurred",
            str(self.operation),
            str(self.message)
        ])


class MissingKeyError(WebsocketException):
    """
    Raised when a required key is missing from WebSocket input data.

    Attributes
    ----------
    key : str
        The missing key name.
    expects : Type
        The type or structure expected.
    """

    def __init__(
        self,
        key: str,
        expects: Type,
        operation: Optional[str] = None,
        kill: bool = False,
        *args,
        **kwargs
    ):
        message = f"Missing Key: {key}"
        data = {
            "key": key,
            "expects": str(expects)
        }
        super().__init__(operation, message, data, kill, *args, **kwargs)


class ExistsError(WebsocketException):
    """
    Raised when a key/value pair is found but should not exist (e.g., duplicate entry).
    """

    def __init__(self, *args, **kwargs):
        data = {
            "detail": f"Key \"{kwargs.get('key', '')}\" of value {kwargs.get('value', '')} already exists"
        }
        super().__init__(message="Key already exists", data=data, *args, **kwargs)


class EmailExistsError(ExistsError):
    """
    Specialized ExistsError for email duplication cases.

    Attributes
    ----------
    email : str
        The email address that already exists.
    """

    def __init__(self, email: str, *args, **kwargs):
        super().__init__(key="Email", value=email, *args, **kwargs)


class NotExistsError(WebsocketException):
    """
    Raised when a required resource or value does not exist.

    Attributes
    ----------
    identifier : str
        The name of the missing field or identifier.
    value : Any
        The specific value that was not found.
    """

    def __init__(self, identifier: str = None, value: Any = None, message: Optional[str] = None, *args, **kwargs):
        
        data = {
            "detail": f"{identifier}:{value} doesn't exist"
        }
            
        if not message:
            message = f"{identifier.capitalize()} doesn't exist"
            
        super().__init__(message=message, data=data, *args, **kwargs)

class UserNotExists(NotExistsError):
    def __init__(self, *args, **kwargs):        
        message = "User doesn't exist"
        super().__init__(message, *args, **kwargs)