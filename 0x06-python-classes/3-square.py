#!/usr/bin/python3

"""Defines a square"""


class Square:
    """This is a square"""

    def __init__(self, size=0):
        """size must be an integerand more than 0"""
        self._Square__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """gives the area of the square"""
        return (self._Square__size ** 2)
