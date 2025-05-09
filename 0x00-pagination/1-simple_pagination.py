#!/usr/bin/env python3
"""Server class module"""
import csv
import math
from typing import List, Tuple


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

    def index_range(self, page: int, page_size: int) -> Tuple:
        """Calculates the range of indexes to return in a list for
        pagination parameters page and page_size

        Parameters:
            page (int): the page number
            page_size (int): the number of values on each page

        Returns:
            A tuple of size two containing a start index and an end index
            corresponding to the range of indexes
        """

        start_index = (page - 1) * page_size
        stop_index = page_size * page

        return (start_index, stop_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Paginate a dataset and return the page(s)

        Parameters:
            page (int): the page number
            page_size (int): number of values on each page

        Returns:
            A list containing the values of the page
        """

        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        dataset = self.dataset()
        indexes = self.index_range(page, page_size)
        if (indexes[0]) > len(dataset):
            return list()

        return dataset[indexes[0]:indexes[1]]
