#!/usr/bin/env python3
"""
file: 1-concurrent_coroutines.py
Desc: This python module contains a python code related to
      asynchronous coroutine programing in python.
Author: Gizachew Bayness
Date Created: Feb 6, 2023
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
