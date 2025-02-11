#!/usr/bin/python3
"""
This is the ``2-append_write`` module
"""


def append_write(filename="", text=""):
    """
    This function append
    """
    with open(filename, "a") as file:
        return file.write(text)
