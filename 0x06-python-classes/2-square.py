#!/usr/bin/python3
"""define a class Square"""


class Square:
    """
    defines properties of a square

    Attributes:
        size: size of a square (1 side)
    """
    def __init__(self, size=0):
        """create new instance of square

        Args:
            size: size of a square (1 side)
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
