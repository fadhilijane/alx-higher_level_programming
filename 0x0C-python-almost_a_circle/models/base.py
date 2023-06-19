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
        """returns the list of the json string rep"""
        l_str = []
        if json_str is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            l_str = json.loads(json_string)
            return l_str

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with all attributes set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ = 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls)
    """returns a list of instances"""
     filename = cls.__name__ + ".json"
     l = []
     lists_dicts = []
     if os.path.exists(filename):
         with open(filename, 'r') as my_file:
             s = my_file.read()
             lists_dicts = cls.from_json_string(s)
             for d in list_dicts:
                 l.append(cls.create(**d))
        return l

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes objs in csv format and saves it to file"""
        if (type(list_objs) != list and list_objs is
            not None or not all(isinstance(x, cls)for x in list_objs)):
            raise TypeError("list_objs must be a list of instances")
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as my_file:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes csv format from file"""
        filename = cls.__name__ + ".csv"
        l = []
        if os.path.exists(filename):
            with open(filename, 'r') as my_file:
                reader = csv.readerr(f, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if e:
                        seattr(i, fields[j], int(e))
                l.append(i)
        return l



