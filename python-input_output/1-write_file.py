#!/usr/bin/python3
"""
Function that writes a string to a text file UTF8
and returns characters written
"""


def write_file(filename="", text=""):
    """
    Write and read file as UTF8
    """
    with open(filename, 'w') as file:
        return file.write(text)