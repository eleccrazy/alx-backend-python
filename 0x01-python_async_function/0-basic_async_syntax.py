#!/usr/bin/python3

"""
file: 0-basic_async_syntax.py
Desc: This python module contains a python code related to
      asynchronous coroutine programing in python.
Author: Gizachew Bayness
Date Created: Feb 6, 2023
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a rundom delay between 0 and max_delay"""
    d = random.uniform(0, max_delay)
    await asyncio.sleep(d)
    return d
