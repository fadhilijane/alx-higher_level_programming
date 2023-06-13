#!/usr/bin/python3
"""Module: 6-load_from_json_file
The function creates an object from a json file
"""


import json


def load_from_json_file(filename):
    """create an object from json file

    Args:
    filename: the json file to be converted
    """
    with open(filename, 'w') as my_file:
        return json.load(my_file)
