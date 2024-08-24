#!/usr/bin/env python3
""" index_range that takes two integer arguments page and page_size. """


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """ index_range that takes two integer arguments page and page_size. """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
