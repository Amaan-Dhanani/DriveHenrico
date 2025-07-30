from typing import Any, Type, TypeVar, Union, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from utils.abc import User


T = TypeVar("T")


class WebsocketMessageContext:
    """The context relating to the specific websocket request message

    Attributes
    ----------
        operation : str
            Current websocket operation, given by the user. Avoid modifying in runtime

        data: Union[dict[str, Any], None]
            Payload the user is sending in
    """

    def __init__(self, operation: str = "unspecified", data: Union[dict[str, Any], None] = None):
        self.operation = operation
        self.data: dict[str, Any] = data

    def cast_data(self, _type: Type[T]) -> T:
        return _type(**self.data)

class WebsocketAuthContext:
    """The context relating to the specific websocket authentication
    
    Attributes
    ----------
        user : Optional[User] = None
            Current user object. Given by the user in auth:token operation

        global_auth : bool = False
            Whether or not authentication is globally required
    
    """
    
    def __init__(self, user: Optional["User"] = None, global_auth: bool = False):
        self.user = user
        self.global_auth = global_auth
        
    @property
    def authenticated(self) -> bool:
        return self.user is not None