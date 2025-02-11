#!/usr/bin/python3
"""
This is the ``6-load_from_json_file`` module
"""
import json


def load_from_json_file(filename):
    """
    This function create an object from a JSON file
    """
    with open(filename, "x") as file:
        json.loads(file)
