#!/usr/bin/env python3
"""
This module defines the function that calculates
the range of indexes
"""


def index_range(page, page_size):
    """
    Return in a list for those particular pagination
    parameters.
    """
    if (page and page_size):
        start = (page - 1) * page_size
        end = start + page_size

    return (start, end)
