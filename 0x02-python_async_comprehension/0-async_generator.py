#!/usr/bin/env python3
"""
file: 0-async_generator.py
Desc: A python module that contains codes related to async
      comprhensions.
Author: Gizachew Bayness
Date Created: Feb 7, 2023
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Generates a sequence of 10 numbers.'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
