#!/usr/bin/python3
"""Module: 9-student
creates a class that defines student
"""


import json


class Student:
    """
    gives public xtics of students
    
    public attribute:
   - first_name
    -last_name
    -age
    """

    def __init__(self, first_name, last_name, age):
        """ object instantion of student

        Args:
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves the dictionary representation of student

        Args:
        self
        Returns a dict of a json obj
        """

        return self.__dict__
