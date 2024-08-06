#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension four times in parallel using asyncio.gather
    """
    start = time.perf_counter()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    finish = time.perf_counter()
    return finish - start
