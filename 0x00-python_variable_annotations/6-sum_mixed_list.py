#!/usr/bin/env python3
""" more complex type annotations """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ a function that returns
        the sum of floats and inegers of a list
    """
    return sum(mxd_lst)
