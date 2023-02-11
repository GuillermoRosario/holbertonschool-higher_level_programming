#!/usr/bin/python3
"""
Function that reads a text file and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads Filename UTF8
    """
    with open(filename, 'g') as file:
        print(file.read(), end="")
