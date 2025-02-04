#!/usr/bin/python3
"""
This is the module ''5-base_geometry''
"""


class BaseGeometry:
    """
    This is the baseclass ''BaseGeometry''
    """

    def __init__(self):
        """
        Does nothing
        """
        pass
    
    def area(self):
        """
        This is the area function
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        This function check if it's an integer or not
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
