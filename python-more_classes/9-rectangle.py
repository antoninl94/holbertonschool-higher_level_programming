#!/usr/bin/python3
"""
This is the '0-rectangle' module.
"""


class Rectangle:
    """
    This is the rectangle class.
    """
    number_of_instances = 0
    print_symbol = "#"
    square = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """
        This is the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        This is the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

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

    @height.setter
    def height(self, value):
        """
        This is the width setter of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def __str__(self):
        rect = ""
        for _ in range(self.height):
            for _ in range(self.width):
                rect += str(self.print_symbol)
            rect += "\n"
        return rect.strip()

    def __repr__(self):
        return str(f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(width=size, height=size)
