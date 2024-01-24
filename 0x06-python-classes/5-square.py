#!/usr/bin/python3
""" defines a square"""


class Square:
    """defines properties of a class Square"""

    def __init__(self, size=0):
        """Initialize square
        Args:
            size (int): size of a square
        """
        self.size = size  # Calls the setter method

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square
        Args:
            value (int): size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value  # Set the size attribute

    def area(self):
        """returns the area of the square

        Returns:
            area (int)
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

