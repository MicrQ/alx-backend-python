#!/usr/bin/env python3
""" python async/await """
import asyncio
import random


async def wait_random(max_delay: int =10) -> float:
    """ waits for a random delay between 0 and max_delay(included) """
    delay = random.uniform(0, max_delay + 1)
    await asyncio.sleep(delay)
    return delay
