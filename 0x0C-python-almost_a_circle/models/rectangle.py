#!/usr/bin/python3
"""Class Rectangle tha inherits form Base"""


import json
from models.base import Base


class Rectangle(Base):
    """The class inherits from Base class

    Args:
    __width-> width
    __height->height
    __x -> x
    __y -> y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            "retrieves the width attribute"""
            return self.__width

        @width.setter
        def width(self, value):
            """sets the width attribute"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            "retrieves the height attribute"""
            return self.__height

        @height.setter
        def height(self, value):
            """sets the height attribute"""
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            "retrieves the x attribute"""
            return self.__x

        @x.setter
        def x(self, value):
            """sets the x attribute"""
            if type(value) is not int:
                raise TypeError("x must be an integer")
            if value <= 0:
                raise ValueError("x must be > 0")
            self.__x = value

        @property
        def y(self):
            "retrieves the y attribute"""
            return self.__y

        @y.setter
        def y(self, value):
            """sets the y attribute"""
            if type(value) is not int:
                raise TypeError("y must be an integer")
            if value <= 0:
                raise ValueError("y must be > 0")
            self.__y = value

        def area(self):
            """gets the area of the rectangle"""
            return self.width * self.height

        def display(self):
            """displays th '#' instead of handling x and y"""
            xter_rep = ''
            for i in range(self.__width):
                for j in range(self.__height):
                    xter_rep += '#'
                xter_rep += '\n'
            return xter_rep[:-1]
