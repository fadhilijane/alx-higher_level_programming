#!/usr/bin/python3
"""Module: 5-save_to_json_file
The function writes an objest to a text file
saving to json file
"""


import json


def save_to_json_file(my_obj, filename):
    """ the fuction writes in the json file

    Args:
    my_obj: the text to be writen in the json file
    filename: the filename
    """

    with open(filename, 'w') as my_file:
        json.dump(my_obj, my_file)
