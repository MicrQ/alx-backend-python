#!/usr/bin/env python3
""" python async/await """
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ waits n times the specified delay """
    # delays = []
    # for i in range(n):
    #     delays.append(await wait_random(max_delay))
    # return sorted(delays)

    return sorted([await wait_random(max_delay) for _ in range(n)])
