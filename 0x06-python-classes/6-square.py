#!/usr/bin/python3
#!/usr/bin/python3
""" defines a square"""


class Square:
    """defines properties of a class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square
        Args:
            size (int): size of a square
            position (tuple): position of the square
        """
        self.size = size  # Calls the setter method
        self.position = position  # Calls the setter method

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

    @property
    def position(self):
        """Retrieve the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square
        Args:
            value (tuple): position of the square
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value  # Set the position attribute

    def area(self):
        """returns the area of the square

        Returns:
            area (int)
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character # and position"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

