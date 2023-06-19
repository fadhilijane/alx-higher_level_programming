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
            for y in range(0, self.__y):
                print()
            for i in range(0, self.__height):
                for x in range(0, self.__x):
                    print(" ", end="")
                for j in range(0, self.__width):
                    print('#', end="")
            print()

        def __str__(self):
            """string representation of a rectangle"""
            return "[Rectangle]({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                          self.__y,
                                                          self.__width,
                                                          self.__height)

        def update(self, *args, **kwargs):
            """updates the __init__ args"""
            if args is notNone and len(args) != 0:
                if len(args) >= 1:
                    if type(args[0]) != int and args[0] is not None:
                        raise TypeError("id must be an integer")
                    self.id = args[0]
                if len(args) > 1:
                    self.width = args[1]
                if len(args) > 2:
                    self.height = args[2]
                if len(args) > 3:
                    self.x = args[3]
                if len(args) > 4:
                    self.y = args[4]
            else:
                for key, value in kwargs.items():
                    if key == "id":
                        if type(value) != int and valueis not None:
                            raise TypeError("id must be integer")
                        self.id = value
                    if key == "width":
                        self.width = value
                    if key == "height":
                        self.height = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

        def to_dictionary(self):
            """Returns dict rep of the rectangle"""
            my_dictionary = {"x": self.x, "y": self.y, "id": self.id,
                             "height": self.height, "width": self.width}
            return my_dictionary
