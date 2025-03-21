#!/usr/bin/python3
"""
This is the ``10-Square`` module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is the ``Square`` subclass
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
