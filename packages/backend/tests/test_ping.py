import sys
sys.dont_write_bytecode = True

import httpx
import pytest

@pytest.mark.asyncio
async def test_ping():
    async with httpx.AsyncClient() as client:
        url = f"http://backend:4000/ping"
        r = await client.get(url)
        assert r.status_code == 200
