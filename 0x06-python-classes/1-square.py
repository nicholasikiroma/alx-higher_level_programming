#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a Square

    Attributes:
        __size(int): size of a side of the square
    """

    def __init__(self, size):
        """Initializes a square

        Args:
            size(int): size of side of the square

        Returns: None
        """
        self.__size = size
