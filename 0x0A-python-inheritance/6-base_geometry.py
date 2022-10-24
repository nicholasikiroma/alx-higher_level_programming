#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class with public attribute called area"""
    def area(self):
        """function raises an exception when called"""
        raise Exception("area() is not implemented")
