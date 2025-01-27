#!/usr/bin/env python

import asyncio
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5510
SLEEP_TIME = 0.5


async def run_client():
    reader, writer = await asyncio.open_connection(HOST, PORT)
    writer.write(b"Hello world!")
    await writer.drain()
    num_messages = 10
    while True:
        data = await reader.read(1024)
        if not data:
            raise Exception("socket closed")
        print(f"Received: {data.decode()!r}")
        if num_messages > 0:
            now = datetime.now()
            await asyncio.sleep(SLEEP_TIME)
            writer.write(now.strftime("%m/%d/%Y %H:%M:%S").encode())
            await writer.drain()
            num_messages -= 1
        else:
            writer.write(b"quit")
            await writer.drain()
            break


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(run_client())
