#!/usr/bin/python3
"""
This is the ``task_01_duck_typing`` module
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    This is the ``Shape`` baseclass
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    This is the ``Circle`` subclass
    """
    def __init__(self, radius=0):
        if not isinstance(radius, int):
            raise TypeError("radius must be an integer")
        if radius < 0:
            raise ValueError("radius must be positive")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

    def perimeter(self):
        return 2*pi*self.radius


class Rectangle(Shape):
    """
    This is the ```Rectangle`` subclass
    """
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2


def shape_info(shape):
    """
    This is the ``shape_info`` function
    """
    if hasattr(shape, 'area') and hasattr(shape, 'perimeter'):
        print("Area: {}".format(shape.area()))
        print("Perimeter: {}".format(shape.perimeter()))
    else:
        raise TypeError
