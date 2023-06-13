#!/usr/bin/python3
"""Module: 4-from_json_string
changes a json string to python representation
"""


import json


def from_json_string(my_str):
    """ the function converts a json str to an object representation

    Args:
    My_str: the json string to be converted
    """

    return json.loads(my_str)
