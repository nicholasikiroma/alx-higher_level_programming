#!/usr/bin/python3

"""Models a Square based on Rectangle parent class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Assigns value to size"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be greater than 0")

        self.width = value
        self.height = value

    def __str__(self):
        """Overwrites str() method"""
        return "[Square] ({}) {} {} - {}/{}".format(self.id,
                                                    self.x, self.y,
                                                    self.width)

    def update(self, *args, **kwargs):
        """Updates class Square"""
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                else:
                    for key, value in kwargs.items():
                        if hasattr(self, key) is True:
                            setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictonary representation of a Square"""
        return {'id': getattr(self, "id"),
                'size': getattr(self, "size"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
