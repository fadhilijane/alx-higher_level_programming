#!/usr/bin/python3
"""module 1-rectangle
Defines a Rectangle class
"""


class Rectangle:
    """Rectangle class is defined by width and height"""
    rectangledict = {}

    def __init__(self, width=0, height=0):
            """Initializes a Rectangle instance
            
            Args:
                width: width of rectangle
                length: length of a rectangle
            """
            self.width = width
            self.height = height
    
    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.width
    
    @width.setter
    def width(self, value):
        """sets the width of the rectangle

        Args:
            value:sets the value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.width = value
    
    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.height
    
    @height.setter
    def height(self, value):
        """sets the width of the rectangle

        Args:
            value:sets the value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("length must be an integer")
        if value < 0:
            raise ValueError("Length must be >= 0")
        self.height = value

    
my_rectangle = Rectangle('seven', 4)
print(my_rectangle.__dict__)

