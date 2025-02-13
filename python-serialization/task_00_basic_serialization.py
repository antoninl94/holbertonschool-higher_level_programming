#!/usr/bin/python3
"""
This is the ``task_00_basic_serialization`` module
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    This function write an object to text file, using a JSON representation
    """
    with open(filename, "w") as file:
        return file.write(json.dumps(data))

def load_and_deserialize(filename):
    """
    This function create an object from a JSON file
    """
    with open(filename, "r") as file:
        return json.load(file)
