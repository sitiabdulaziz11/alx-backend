#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    function that calculates the start and an end index for pagination.
    """

    if page == 1:
        start_index = 0
    else:
        start_index = (page - 1) * page_size

    end_index = start_index + page_size
    return start_index, end_index
