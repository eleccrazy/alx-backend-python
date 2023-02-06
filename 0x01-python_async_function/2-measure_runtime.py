#!/usr/bin/env python3
"""
file: 2-measure_runtime.py
Desc: This python module contains a python code related to
      asynchronous coroutine programing in python.
Author: Gizachew Bayness
Date Created: Feb 6, 2023
"""
from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime """
    start = time()

    run(wait_n(n, max_delay))

    end = time()

    return (end - start) /n
