#!/usr/bin/python3
"""
This is the ''3-is_kind of class'' module, and it returns True
if the object is an instance of, or if the object is an instance
of a class that inherited from, the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Return ''True'' if the object is an instance of, or is a instance
    of a class that inherited from the specified class
    """
    return isinstance(obj, a_class)
