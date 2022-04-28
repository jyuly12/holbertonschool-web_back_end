#!/usr/bin/env python3
"""
    Annotate the below functions parameters and return
    values with the appropriate types

    Initial code:
    def element_length(lst):
        return [(i, len(i)) for i in lst]
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Module Solution
    """
    return [(i, len(i)) for i in lst]
