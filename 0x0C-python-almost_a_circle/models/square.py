#!/usr/bin/python3

"""Models a Square based on Rectangle parent class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overwrites str() method"""
        str_rectangle = '[Square] '
        str_id = '({}) '.format(self.id)
        str_xy = '{}/{} - '.format(self.x, self.y)
        str_wh = '{}/{}'.format(self.width, self.height)

        return str_rectangle + str_id + str_xy + str_wh

    @property
    def size(self):
        """Retrieves the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Assigns value to size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Overwrites str() method"""
        str_rectangle = '[Square] '
        str_id = '({}) '.format(self.id)
        str_xy = '{}/{} - '.format(self.x, self.y)
        str_size = '{}'.format(self.size)

        return str_rectangle + str_id + str_xy + str_size

    def update(self, *args, **kwargs):
        """Updates class Square"""
        if args is not None and len(args) is not 0:
            list_attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_attr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictonary representation of a Square"""
        return {'id': getattr(self, "id"),
                'size': getattr(self, "size"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
