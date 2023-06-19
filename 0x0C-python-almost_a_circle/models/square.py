#!/usr/bin/python3
"""The square module will inherit properties from the rectangle"""


from base import Base
from rectangle import Rectangle


class Square(Rectangle):
    """describes a square

    public instance method:
    - area()
    - display()
    - to_dictionary()
    - update()
    these come from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructs the square class

        Args:
        - __size
        - __x
        - __y
        -id
        """

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str rep of the square"""
        s = "[Square]({}) {}/{}-{}".format(self.id,
                                           self.x, self.y, self.__width)
        return s

    @property
    def size(self):
        """retrieves the size attribut"""
        return self.__width

    @size.setter
    def size(self, value):
        """set the size attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError(" width musebe >0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """updates the attributes into the given numbers)"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.item():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """dictionary representation of a square"""
        my_dictionary = {'id': self.id, 'x': self.x,
                         'size': self.size, 'y': self.y}
        return my_dictionary
