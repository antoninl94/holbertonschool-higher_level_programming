#!/usr/bin/python3
"""
This is the 4-print_square module.

>>> print_square(4)
####
####
####
####
"""


def print_square(size):
    """
    This function print a "#" square of size "size".
    """
    if not isinstance(size, int):
        raise Exception('size must be an integer')
    if size < 0:
        raise Exception('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
