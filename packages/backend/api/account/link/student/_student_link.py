# === Core ===
from dataclasses import dataclass

# === Utilities ===
from utils import websocket_auth, websocket_message
from utils.abc import Invite

# === Errors ===
from utils.exception.websocket import WebsocketException


@dataclass
class D:
    invite_code: str


async def student_link(*_, **__):
    """
    Operation used whenever a student wants to use an invite code to link to either
    a parent or a class

    :param str invite_code: Invite Code used

    :raises WebsocketException:

        - If the user doesn't exist

        - If the user isn't a student account

        - If the student is already linked to the type of invite
        For example, if the invite_code links to a parent, and the student
        is already linked to a parent. Raises

        - If the student is already linked to that specific invite target,
        If a student is already linked to the parent in question or class in question, raise.

    """

    data: D = websocket_message.cast_data(D)

    user = websocket_auth.user

    if user is None:
        raise WebsocketException(operation="link:rejected", message="User isn't specified, did you auth?")

    if not user.is_student:
        raise WebsocketException(operation="link:rejected", message="You are not a student")

    try:
        invite = Invite.get(code=data.invite_code)
    except LookupError:
        raise WebsocketException(operation="link:rejected", message="Invite doesn't exist")

    # Link user all in one
    invite.link(user)

    return "link:success", {}
