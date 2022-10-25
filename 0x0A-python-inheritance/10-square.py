#!/usr/bin/python3
"""Module contains the class BaseGeometry and subclass Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Models a square"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates area of the square"""
        return self.__size ** 2
