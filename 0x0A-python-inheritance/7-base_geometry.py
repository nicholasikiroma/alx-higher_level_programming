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
