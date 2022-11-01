#!/usr/bin/python3
"""Defines a derived class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle based on superclass Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instances of Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for private attribute width
        Returns: self.__width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be greater than 0")
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
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be greater than 0")

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
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value <= 0:
            raise ValueError("x must be greater than 0")

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
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value <= 0:
            raise ValueError("y must be greater than 0")

        self.__y = value

    def area(self):
        """Returns area of Rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """prints Rectangle instance to the stdout"""
        rectangle = ""

        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """Overwrites str() method"""
        return "[Rectangle] ({}) {} {} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
                return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """Returns dictonary representation of a Rectangle"""
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, 'width')}
