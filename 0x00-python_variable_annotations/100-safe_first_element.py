#!/usr/bin/env python3
"""
    Given the parameters and the return values
    add type annotations to the function

    def safe_first_element(lst):
        if lst:
            return lst[0]
        else:
            return None
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Module Solution"""
    if lst:
        return lst[0]
    else:
        return None
