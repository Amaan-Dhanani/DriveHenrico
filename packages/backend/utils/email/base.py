from typing import Optional
from utils.helper.config import Yaml
from email.message import EmailMessage
import aiosmtplib

_yml_conf = Yaml()
_email_conf = _yml_conf.get("backend.email")

class BaseEmail:        
    def __init__(self, to: str, subject: Optional[str]) -> None:
        self._email = EmailMessage()
        self._email["From"] = _email_conf["username"]
        self._email["To"] = to
        self._email["Subject"] = subject
        
    async def send(self):        
        self._email.set_content(getattr(self, "content", "No Content"))
        await aiosmtplib.send(self._email, **_email_conf)
    
    

