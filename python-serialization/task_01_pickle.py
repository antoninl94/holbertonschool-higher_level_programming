#!/usr/bin/python3
"""
This is the ``task_01_pickle`` module
"""
import pickle


class CustomObject:
    """
    This is the ``CustomObject`` class
    """
    def __init__(self, name="", age=0, is_student=True):
        self.name = name
        self.age = age
        self.is_student = is_student

    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as file:
            return pickle.load(file)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                return pickle.dump(self, file)
        except Exception:
            return
