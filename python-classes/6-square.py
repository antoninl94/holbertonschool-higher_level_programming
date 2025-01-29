#!/usr/bin/python3
"""
This is the '0-square' module.
"""


class Square:
    """
    This is the square class.
    """
    def __init__(self, size=0, position=(0, 0)):
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(position) > 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__position = position
        self.__size = size

    def area(self):
        """
        This is the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        This is the size getter
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        This is the size setter
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def position(self):
        """
        This is the position getter
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This is the position setter
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """
        This method print a square depending of size
        """
        if self.size == 0:
            print()
            return
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + '#' * self.size)
