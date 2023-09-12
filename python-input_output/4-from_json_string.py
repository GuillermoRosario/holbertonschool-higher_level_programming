#!/usr/bin/python3
"""
Imports Json function
"""
import json


def from_json_string(my_str):
    """
    Function that returns a Python object
    represented by a JSON string
    """
    return json.loads(my_str)
