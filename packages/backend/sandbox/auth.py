
from dataclasses import dataclass
from utils.console import console

import websockets
from used_json import *

@dataclass
class Credential:
    email: str
    password: str

parent = Credential(email="parent@parent.com", password="parent")    
student = Credential(email="student@student.com", password="student")
teacher = Credential(email="teacher@teacher.com", password="teacher")

STUDENT_TOKEN = "803a5e29133cbe19c4a9b25dfb3006d9485290218e1fdd952df0ada1f20bc295"
TEACHER_TOKEN = "c8a87b1b6c10e6d218a9c7b0847ee91a943c1119aca0095460788c8a5d31d6c6"
PARENT_TOKEN = "9b2130def94901455d36b582af39f0a411fb2d390ea8b3929c6463a7d62e3115"

async def auth_as(websocket: websockets.ClientConnection, token: str):
    _payload_auth = to_json({
        "operation": "auth:token",
        "data": {
            "token": token
        }
    })
    
    await websocket.send(_payload_auth)
    
    response = from_json(await websocket.recv())
    
    if response["operation"] != "auth:success":
        print(response)
        quit()
        
    console.debug("Authenticated")