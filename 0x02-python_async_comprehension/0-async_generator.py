#!/usr/bin/env python3
"""
This module generate ramdom values
"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """generates random number between 0 and 10."""
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
