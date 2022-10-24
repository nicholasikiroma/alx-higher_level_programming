#!/usr/bin/python3
"""
Module contains inherits_from function
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited"""
    return (issubclass(obj, a_class) and type(obj) != a_class)
