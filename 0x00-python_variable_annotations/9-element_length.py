#!/usr/bin/env python3
""" more complex annotations """

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ a function that returns """
    return [(i, len(i)) for i in lst]
