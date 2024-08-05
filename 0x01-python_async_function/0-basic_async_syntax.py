#!/usr/bin/env python3
"""
async/ await function
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    A function that waits for a random time and returns it
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
