#!/usr/bin/python3
"""
This is the 0-add_integer module.

The 0-add_integer module supplies one function, add_integer(). For exemple,
>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """
    Add two numbers and return the sum.
    """
    try:
        if not isinstance(a, int) and not isinstance(a, float):
            raise TypeError("a must be an integer")
        if not isinstance(b, int) and not isinstance(b, float):
            raise TypeError("b must be an integer")
        if isinstance(a, float):
            a = int(a)
        if isinstance(b, float):
            b = int(b)
    except TypeError as te:
        return te
    return a + b
