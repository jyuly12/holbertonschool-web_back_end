#!/usr/bin/env python3
"""
This module defines sum_list function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list input_list of floats as argument.
    Returns their sum as a float.
    """
    value = 0    
    for item in input_list:
        value += item
    return float(value)
