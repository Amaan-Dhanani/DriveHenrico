import sys
sys.dont_write_bytecode = True

import asyncio
import pytest_asyncio
import httpx

from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.helper.config import Yaml


@pytest_asyncio.fixture(scope="session", autouse=True)
async def wait_for_app():
    url = f"http://backend:4000/health"
    print("url", url)
    for _ in range(30):
        try:
            async with httpx.AsyncClient() as client:
                r = await client.get(url)
                if r.status_code == 200:
                    print("all gud")
                    return
        except:
            pass
        await asyncio.sleep(1)
    raise RuntimeError("Quart app did not start in time.")
