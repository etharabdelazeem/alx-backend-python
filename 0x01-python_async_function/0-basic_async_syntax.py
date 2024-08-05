#!/usr/bin/env python3

""" A function that waits for a random time and returns it"""
import asyncio
import random

async def wait_random(max_delay=10):
    delay = random.uniform(0,max_delay) 
    await asyncio.sleep(delay);
    return delay;
