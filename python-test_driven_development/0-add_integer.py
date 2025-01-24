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
        if not isinstance(a, int):
            raise TypeError("a must be an integer")
        if not isinstance(b, int):
            raise TypeError("b must be an integer")
        #if isinstance(a, float):
        return a + b
    except TypeError as te:
        print(te)
