from typing import Any, Type, TypeVar, Union


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
