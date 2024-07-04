#!/usr/bin/env python3
""" more complex type annotations """

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ a function that returns the first element of a sequence
        object or None
    """
    if lst:
        return lst[0]
    else:
        return None
