import json

def to_json(data: dict) -> str:
    return json.dumps(data)


def from_json(data: str) -> dict:
    return json.loads(data)