#!/usr/bin/python3
""" class defines a student"""


class Student:
    """shows the sttributes of a student"""

    def __init__(self, first_name, last_name, age):
        """ initialize student

        Args:
        -first_name
        -last_name
        -age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dict rep of student

        Args:
        -self
        -attrs: only attribut names in the list
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
