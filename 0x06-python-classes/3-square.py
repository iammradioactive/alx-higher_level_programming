#!/usr/bin/python3
""" defines a square"""


class Square:
    """defines properties of a class Square"""

    def __init__(self, size=0):
        """Initialize square
        Args:
            size (int): size of a square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size #: size of square

def area(self):
    """returns the area

    Returns:
        area
    """
    return self.__size**2
