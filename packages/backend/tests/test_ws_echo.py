import pytest
import websockets
import asyncio

@pytest.mark.asyncio
async def test_ws_echo():
    uri = "ws://backend:4000/ws/echo"
    async with websockets.connect(uri) as ws:
        await ws.send("hello")
        response = await ws.recv()
        assert response == "hello"
