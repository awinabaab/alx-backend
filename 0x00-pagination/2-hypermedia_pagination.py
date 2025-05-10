#!/usr/bin/env python3
"""Server class module"""
import csv
import math
from typing import List, Tuple, Dict, Union
import math


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

    def get_hyper(self,
                  page: int = 1,
                  page_size: int = 10
                  ) -> Dict[str, Union[int, str, List[str], None]]:
        """Paginate a dataset and return the page(s)

        Parameters:
            page (int): the page number
            page_size (int): number of values on each page

        Returns:
            A dictionary containing:
            - page (int): the current page number
            - page_size (int): the number of values per page
            - data (list): the data of the page
            - next_page (int): the next page's number
            - prev_page (int): the previous page's number
        """

        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = None if page + 1 > total_pages else page + 1
        prev_page = None if page - 1 < 1 else page - 1

        hyper_dataset = {
                         "page": page,
                         "page_size": page_size,
                         "data": data,
                         "next_page": next_page,
                         "prev_page": prev_page,
                         "total_pages": total_pages
                         }

        return hyper_dataset
