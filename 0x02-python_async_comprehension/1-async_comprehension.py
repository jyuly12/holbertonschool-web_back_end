#!/usr/bin/env python3
"""
This module uses Asynchronous Comprehensions
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Asynchronous Comprehensions"""
    return [i async for i in async_generator()]
