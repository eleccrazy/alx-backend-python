#!/usr/bin/env python3
"""
file: 0-async_generator.py
Desc: A python module that contains codes related to async
      comprhensions.
Author: Gizachew Bayness
Date Created: Feb 7, 2023
"""
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Creates a list of 10 numbers from a 10-number generator.'''
    return [num async for num in async_generator()]
