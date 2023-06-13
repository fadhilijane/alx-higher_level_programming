#!/usr/bin/python3
""" module: 2-append_write
appends text at the end of a string
"""


def append_write(filename="", text=""):
    """The function appends characters at the end of the string

    Args:
    filename- name of the text file
    text- text to be appended
    """

    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
