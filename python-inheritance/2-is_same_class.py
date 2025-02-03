#!/usr/bin/python3
"""
This is the ''2-is_same_class'' module that return 'True' if
the object is exactly an instance of the specified class, otherwise
return 'False'
"""


def is_same_class(obj, a_class):
    """
    This function return True if the object is an instance
    of the specified class, otherwise False
    """

    return type(obj) is a_class
