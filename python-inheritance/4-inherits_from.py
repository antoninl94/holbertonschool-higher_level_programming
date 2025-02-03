#!/usr/bin/python3
"""
This is the ''4-inherits_from'' module
"""


def inherits_from(obj, a_class):
    """
    Return True if the object inherits from the specified class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
