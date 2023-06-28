#!/usr/bin/python3
"""
Module with class 'Base
"""
import json

class Base:
    """
    'base' manages the id attributes in all future classes and 
    avoids duplicating the same code
    """
    _nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
