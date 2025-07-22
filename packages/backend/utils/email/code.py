from typing import Union
from .base import BaseEmail


class CodeEmail(BaseEmail):
    
    def __init__(self, to: str, code: Union[str, int]) -> None:
        self.__code = code
        super().__init__(to, subject="Your DriveHenrico Code")
    
    @property
    def content(self) -> str:
        return f"Your DriveHenrico Code is {self.__code}"