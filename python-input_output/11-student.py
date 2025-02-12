#!/usr/bin/python3
"""
This is the ``9-student`` module
"""


class Student:
    """
    This is the ``Student`` class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return vars(self)
        return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
