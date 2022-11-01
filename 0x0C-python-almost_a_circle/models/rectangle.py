#!/usr/bin/python3
"""Defines a derived class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle based on superclass Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instances of Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for private attribute width
        Returns: self.__width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        self.setter_validation('width', value)
        self.__width = value

    @property
    def height(self):
        """Getter for private attribute width
        Returns: self.__height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        self.setter_validation('height', value)
        self.__height = value

    @property
    def x(self):
        """Getter for private attribute x
        Returns: self.__x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        self.setter_validation('x', value)
        self.__x = value

    @property
    def y(self):
        """Getter for private attribute y
        Returns: self.__y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        self.setter_validation('y', value)
        self.__y = value

    def area(self):
        """Returns area of Rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """prints Rectangle instance to the stdout"""
        y_offset = '\n' * self.y
        x_offset = ' ' * self.x
        print(y_offset, end='')
        for i in range(self.height):
            print(x_offset, '#' * self.width, sep='')

    def __str__(self):
        """Overwrites str() method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args is not None and len(args) is not 0:
            list_attr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictonary representation of a Rectangle"""
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, 'width')}

    @staticmethod
    def setter_validation(attribute, value):
        """Validates setter"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == 'x' or attribute == 'y':
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))
