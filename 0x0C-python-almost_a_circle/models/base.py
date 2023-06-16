#!/usr/bin/python3
"""we are creating a base class"""


Class Base:
    """This is the base class

    Args:
    __nb_objects
    """
    __nb_objects = 0

    def__init__(self, id=None):
        """initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
