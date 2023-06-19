#!/usr/bin/python3
"""we are creating a base class"""


import json
import os
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a JSON representation of list-dictionaries"""
        if list_dictionaries is None of list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or not all(type(x) 
            == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write json str rep to list_objs"""
        if list_objs is None or list_objs == []:
            j_str = "[]"
        else:
            j_str = cls.to_json_string([o.to_dictionary() for o in list_objs])
            filename = cls.__name__ + ".json"
            with open(filename, 'w') as my_file:
                my_file.write(j_str)

    @staticmethod
    def from_json_string(json_string):

