#!/usr/bin/env python

import asyncio


async def count(n):
    for i in range(1, n + 1):
        print(i)
        await asyncio.sleep(0)
    return n


# async def main():
#     async with asyncio.TaskGroup() as tg:
#         tg1 = tg.create_task(count(5))
#         tg2 = tg.create_task(count(10))
#     print(f"Result of tg1: {tg1.result()}")
#     print(f"Result of tg2: {tg2.result()}")
#     print("Done!")


# throws an exception group
async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(count(5))
        tg.create_task(count(10))
        tg.create_task(count("10"))
        tg.create_task(count(10.0))


if __name__ == "__main__":
    asyncio.run(main())
