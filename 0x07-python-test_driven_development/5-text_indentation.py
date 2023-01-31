#!/usr/bin/python3
"""
Module text_indentation
prints a text with 2 new lines
Adds 2 new lines after a set of characters.
"""


def text_indentation(text):
    """
    Prints a text and add two newlines
    after each of these characters {'.', '?', ':'}.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
