from typing import TypedDict

class T_Credential(TypedDict):
    salt: str
    hashed: str
    email: str
    account_id: str