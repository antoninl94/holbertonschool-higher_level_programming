#!/usr/bin/python3
"""
This is the ``5-save_to_json_file`` module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function write an object to text file, using a JSON representation
    """
    with open(filename, "w") as file:
        return file.write(json.dumps(my_obj))
