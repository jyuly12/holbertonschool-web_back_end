#!/usr/bin/env python3
"""
This module defines the function that calculates
the range of indexes
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Return in a list for those particular pagination
    parameters.
    """
    if (page and page_size):
        start = (page - 1) * page_size
        end = start + page_size

    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Takes two integer arguments page with default value 1 and
        page_size with default value 10.
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        start, end = index_range(page, page_size)
        pages = []
        if start >= len(self.dataset()):
            return pages
        pages = self.dataset()
        return pages[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """
        Takes the same arguments (and defaults) as get_page and
        returns a dictionary
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        total = math.floor(len(self.dataset()) / page_size)
        new_dic = {
                    'page_size': len(self.get_page(page, page_size)),
                    'page': page,
                    'data': self.get_page(page, page_size),
                    'next_page': page + 1 if page + 1 < total else None,
                    'prev_page': page - 1 if page > 1 else None,
                    'total_pages': total}

        return new_dic
