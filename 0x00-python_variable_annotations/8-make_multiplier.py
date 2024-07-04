#!/usr/bin/env python3
""" more complex type annotations """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ a funtion that returns a callable function """
    return lambda val: multiplier * val
