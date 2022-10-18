#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a Square

    Attributes:
        __size(int): size of a side of the square
    """

    def __init__(self, size=0):
        """Initializes a square

        Args:
            size(int): size of side of the square

        Returns: None
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size

        else:
            raise TypeError("size must be an integer")
