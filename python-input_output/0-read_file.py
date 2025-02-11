#!/usr/bin/python3
"""
This is the ``read_file`` module
"""


def read_file(filename=""):
    """
    This function read a file and print de it to stdout
    """
    with open(filename, "r") as file:
        print(file.read(), end="")
