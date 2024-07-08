#!/usr/bin/env python3
""" python async/await """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ waits n times the specified delay """
    return [await task for task in
            asyncio.as_completed(
                [asyncio.create_task(wait_random(max_delay))
                 for _ in range(n)]
                 )]
