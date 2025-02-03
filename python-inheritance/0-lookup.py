#!/usr/bin/python3
"""
This module return a list of availables
attributes and methods of an object.
"""
def lookup(obj):
    return list(dir(obj))
