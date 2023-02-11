#!/usr/bin/python3
"""
Imports Json function
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to
    a text file using JSON """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
