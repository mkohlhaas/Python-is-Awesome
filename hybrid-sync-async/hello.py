#!/usr/bin/env python

import asyncio
from pathlib import Path

import aiofiles
import xsync


# xsync library is obosete!


class Reader:
    @xsync.as_hybrid()
    def read_text(path: Path) -> str:
        with open(path) as f:
            return f.read().strip()

    @xsync.set_async_impl(read_text)
    async def async_read_text(path: Path) -> str:
        async with aiofiles.open(path) as f:
            return (await f.read()).strip()


if __name__ == "__main__":
    r = Reader()
    txt: str = r.read_text(Path("topsecret.txt"))
    print(txt)

    async def main():
        await r.async_read_text("topsecret.txt")

    asyncio.run(main())
