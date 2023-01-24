#!/usr/bin/python3

"""Define a square"""


class Square:
    """size where size must be an integer"""

    def __init__(self, size=0):
        """initialize the square"""
        self._Square__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
