#!/usr/bin/python3
"""
This is the '0-square' module.
"""


class Square:
    """
    This is the square class.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
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

    def my_print(self):
        """
        This method print a square depending of size
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print('#', end="")
                print()
