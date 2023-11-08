#!/usr/bin/python3
"""
    append after module
"""


def append_after(filename="", search_string="", new_string=""):
    """
        function that inserts a line of text to a file
        after each line containing a specific string
    """
    with open(filename, "r+", encoding="utf-8") as myFile:
        s = ""
        for line in myFile:
            s += line
            if search_string in line:
                s += new_string
        myFile.seek(0)
        myFile.write(s)
