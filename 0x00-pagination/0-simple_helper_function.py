#!/usr/bin/env python3
"""Calculates the range of indexes to return in a list"""
from typing import Tuple


def index_range(page, page_size) -> Tuple:
    """Calculates the range of indexes to return in a list for
    pagination parameters page and page_size

    Parameters:
        page (int): the page number
        page_size (int): the number of values on each page

    Returns:
        A tuple of size two containing a start index and an end index
        corresponding to the range of indexes"""

    start_index = (page - 1) * page_size
    stop_index = page_size * page

    return (start_index, stop_index)
