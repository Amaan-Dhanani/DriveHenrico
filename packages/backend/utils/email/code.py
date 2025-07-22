from typing import Union
from .base import BaseEmail


class CodeEmail(BaseEmail):
    """
    Sends a DriveHenrico code to the user via email.

    Constructs the message content and prepares everything
    for sending through SMTP using the BaseEmail interface.

    :param str to: The recipient's email address
    :param Union[str, int] code: The verification or login code to send
    """

    def __init__(self, to: str, code: Union[str, int]) -> None:
        self.__code = code
        super().__init__(to, subject="Your DriveHenrico Code")

    @property
    def content(self) -> str:
        """
        Content of the email, dynamically generated using the code.

        :return: Plaintext message to be sent in the email body
        """
        return f"Your DriveHenrico Code is {self.__code}"
