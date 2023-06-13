#!/usr/bin/python3
"""Module: 8-class_to_json
Returns the dictionary display
"""


def class_to_json(obj):
    """Returnd a simple data structure for JSON

    Args:
    obj: object to be looked at(opened)
    """

    return obj.__dict__
