#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class with public attribute called area"""
    def area(self):
        """function raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function validates value received

        Args:
            name(string) - input name
            value(int) - integer value
        """
        if type(value) is not int:
            raise TypeError("{:s} must be integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Subclass of BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height
 
    def __str__(self):
        """string representation of rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
