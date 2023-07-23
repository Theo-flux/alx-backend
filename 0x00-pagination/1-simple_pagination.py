#!/usr/bin/env python3
"""
simple pagination module
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """_summary_

    Args:
        page (int): page number
        page_size (int): the number of docs per page

    Returns:
        Tuple: _description_
    """
    total_doc = page*page_size
    starting_point = (page-1)*page_size

    return (starting_point, total_doc)


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
        """_summary_

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            List[List]: _description_
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset_range = index_range(page, page_size)

        if dataset_range[1] > len(self.dataset()):
            return []

        return self.dataset()[dataset_range[0]:dataset_range[1]]
