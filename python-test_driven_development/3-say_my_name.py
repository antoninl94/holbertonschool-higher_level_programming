#!/usr/bin/python3
"""
This is the 3-say_my_name module.

>>> say_my_name("John", "Doe")
My name is John Doe
"""


def say_my_name(first_name, last_name=""):
    """
    Print the First name and the Last name preceded by "My name is"
    """
    if not isinstance(first_name, str):
        raise Exception("first_name must be a string")
    if not isinstance(last_name, str):
        raise Exception("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
