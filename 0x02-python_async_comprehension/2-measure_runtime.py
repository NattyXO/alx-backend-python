#!/usr/bin/env python3
""" asyncio.gather """

import asyncio
import random
import timeit
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime(loop: asyncio.AbstractEventLoop) -> float:
    """ Executes comprehension func 4 times in parallel, returns runtime """
    start = timeit.default_timer()
    coroutines: List[asyncio.Task] = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coroutines, loop=loop)
    stop = timeit.default_timer()
    return stop - start


async def main() -> float:
    async with asyncio.get_event_loop() as loop:
        return await measure_runtime(loop)


if __name__ == "__main__":
    print(asyncio.run(main()))
