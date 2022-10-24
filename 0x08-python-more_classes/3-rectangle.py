#!/usr/bin/python3
"""Models a Rectangle"""


class Rectangle:
    """Represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """"Initializes the Rectangle

        Args:
            width(int): defines the width of the rectangle
            height(int): defines the height of the rectangle

        Returns: None
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Retrieves private instance attribute width

            Returns: self.__width
            """
            return self.__width

        @width.setter
        def width(self, value):
            """Setter for private instance attribute width

            Returns: self
            """
            if type(value) is not int:
                raise TypeError("width must be an integer")

            if value < 0:
                raise ValueError("width must be >= 0")

            self.__width = value

        @property
        def height(self):
            """Retrieves private instance attribute width

            Returns: self.__height
            """
            return self.__height

        @height.setter
        def height(self, value):
            """Setter for private instance attribute height"""
            if type(value) is not int:
                raise TypeError("height must be an integer")

            if value < 0:
                raise ValueError("height must be >= 0")

            self.__width = value

        def area(self):
            """Calculates the area of a rectangle

            Returns: width * height
            """
            return self.__width * self.__height

        def perimeter(self):
            """Calculates the area of a rectangle

            Returns: width * height
            """
            if self.__width == 0 or self.__height == 0:
                return 0

            return 2 * (self.__width + self.__height)

        def __str__(self):
            """returns printable string representaion of the rectangle"""
            string = ""
            if self.__height != 0 and self.__width != 0:
                string += "\n".join("#" * self.__width
                                    for j in range(self.__height))
            return string
