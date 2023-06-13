#!/usr/bin/python3
"""module: 3-to_json_string
Returns the string representation of an object
"""


import json


def to_json_string(my_obj):
    """The function returns the JSON presentation of an object

    Args:
    my_obj: it is the object to be converted to the JSON data
    """
    return json.dumps(my_obj)
