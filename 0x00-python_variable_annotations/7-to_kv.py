#!/usr/bin/env python3
"""
This module defines "to_kv" function.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int OR float v as arguments.
    Returns a tuple.
    """
    value: Tuple[srt, Union[int, float]]
    value = (k, v ** 2)
    return value
