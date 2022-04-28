#!/usr/bin/env python3
"""
This module defines "sum_mixed_list" function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list mxd_lst of integers and floats.
    Returns their sum as a float.
    """
    value = 0    
    for item in mxd_lst:
        value += item
    return float(value)
