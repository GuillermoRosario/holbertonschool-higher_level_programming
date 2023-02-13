#!/usr/bin/python3
"""
Create a class named 'Base'
"""


class Base:
    """
    Base comment Module
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
