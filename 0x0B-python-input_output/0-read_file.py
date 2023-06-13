#!/usr/bin/python3
"""module: 0-read_file
the function reads the text file provided
"""
def read_file(filename=""):
    """ Reads the txt file and shows in the stdout
    Args:
    -filename: file to be read
    """
    with open(filename, encoding="utf-8") as theFile:
        print(theFile.read())
