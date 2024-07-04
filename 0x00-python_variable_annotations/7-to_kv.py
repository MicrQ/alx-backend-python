#!/usr/bin/env python3
""" more complex type annotations """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ a function that returns tuple of given args """
    return (k, v ** 2)
