#!/usr/bin/python3
"""Module contains MyInt"""


class MyInt(int):
    """rebel version of an integer"""
    def __new__(cls, *args, **kwargs):
        """creates a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """altering eq method"""
        return int(self) != other

    def __ne__(self, other):
        """altering ne method"""
        return int(self) == other
