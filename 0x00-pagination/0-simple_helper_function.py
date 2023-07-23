#!/usr/bin/env python3
"""
simple helper function module
"""
from typing import Tuple


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
