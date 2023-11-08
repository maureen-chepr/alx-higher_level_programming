#!/usr/bin/python3
"""
    function that appends a string
"""


def append_write(filename="", text=""):
    """
        function that appends a string at the end of a text file
        and returns the number of characters
    """

    with open(filename, "a", encoding="utf-8") as myFile:
        myFile.write(text)
    return len(text)
