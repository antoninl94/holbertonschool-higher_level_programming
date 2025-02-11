#!/usr/bin/python3
"""
This is the ``1-write_file`` module
"""


def write_file(filename="", text=""):
    """
    This function print ``text`` in the file ``filename``
    """
    with open(filename, "w") as file:
        return file.write(text)
