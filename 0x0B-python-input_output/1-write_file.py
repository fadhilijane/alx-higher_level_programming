#!/usr/bin/python3
""" module: 1-write_file
writes a string to a txt file
"""


def write_file(filename="", text=""):
    """Writes text in a newfile

    Args:
    filename: new file created
    text: text written
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
        text_length = len(text)
        return (text_length, end="")
