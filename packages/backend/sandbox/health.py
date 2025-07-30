from utils.console import console
import asyncio


async def health(client, route):
    route_health = f"{route}/health"
    console.log(f"Health Check {route_health}")
    for _ in range(30):
        try:
            response = await client.get(route_health)
            console.debug(response)
            if response.status_code == 200:
                return
        except Exception as e:
            pass
        console.log("Waiting...")
        await asyncio.sleep(1)
    raise RuntimeError("Backend didn't run in time")