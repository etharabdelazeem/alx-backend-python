#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
from time import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension four times in parallel using asyncio.gather
    """
    start = time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    finish = time()
    return finish - start
