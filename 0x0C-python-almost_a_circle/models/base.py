#!/usr/bin/python3
"""Module contains parent class called Base"""


class Base:
    """Represents the model for all other classes in the project

    Attributes:
        __nb_objects(int): Records the number of instances created
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation of Base.

        Args:
            id(int): Identity of class instance
        """
        if id is not None:
            self.id = id
        else:    
            __nb_objects += 1
            self.id = Base.__nb_objects 
