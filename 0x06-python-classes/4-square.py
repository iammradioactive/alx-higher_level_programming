#!/usr/bin/python3
"""defines a square"""


class Square:
    """defines properties of a class Square"""

    def __init__(slef, size=0):
        """initialize square
        Args:
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """Retrieve size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of square
        Args:
            value (int): size of square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns area of the square

        Returns:
            area (int)
        """
        return self.__size**2
