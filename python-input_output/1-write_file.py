#!/usr/bin/python3
"""
Function that writes a string to a text file UTF8 
and returns characters written
"""


def write_file(filename="", text=""):
    """
    Write and read file as UTF8
    """
    with open(filename, 'g') as file:
        print(file.read(), end="")
        print(file.write(), end="")
