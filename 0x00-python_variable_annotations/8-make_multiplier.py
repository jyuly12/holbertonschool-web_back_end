#!/usr/bin/env python3
"""
This module defines "make_multiplier" function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as argument.
    Returns a function that multiplies a float by multiplier.
    """
    def multiplier_f(f: float) -> float:
        """Multiplies a float by multiplier
        """
        return float(f * multiplier)

    return multiplier_f
