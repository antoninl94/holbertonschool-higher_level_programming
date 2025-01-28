#!/usr/bin/python3
"""
This is the '0-rectangle' module.
"""


class Rectangle:
    """
    This is the rectangle class.
    """
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError('height must be an integer')
        if width < 0:
            raise ValueError('height must be >= 0')
        if not isinstance(height, int):
            raise TypeError('width must be an integer')
        if height < 0:
            raise ValueError('width must be >= 0')
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        This is the width getter of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This is the width setter of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        This is the width getter of the rectangle
        """
        return self.__height

    @width.setter
    def height(self, value):
        """
        This is the width setter of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
