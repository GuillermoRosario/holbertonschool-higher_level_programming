#!/usr/bin/python3
"""
Imports Json function
"""
import json


def load_from_json_file(filename):
    """
    Create an Object from a JSON File
    """
    with open(filename, 'r') as file:
        str = file.read()
        return json.loads(str)
