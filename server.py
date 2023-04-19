import asyncio
from app import app
from hypercorn.asyncio import serve
from hypercorn.config import Config
from discord_bot import client

async def my_serve(app, host, port):
    config = Config()
    config.bind = [f"{host}:{port}"]
    await serve(app, config)

async def start():
    await my_serve(app=app, host="0.0.0.0", port=32450)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(client.start(os.getenv("DISCORD_TOKEN")))
    loop.create_task(start())
    loop.run_forever()
