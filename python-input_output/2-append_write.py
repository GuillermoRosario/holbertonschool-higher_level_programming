#!/usr/bin/python3
"""
Function that appends a string at the end
of a text file, Returns the characters added
"""


def append_write(filename="", text=""):
    """
     Append Function
    """
    with open(filename, 'a') as file:
        return file.write(text)
