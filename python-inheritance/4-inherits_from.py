#!/usr/bin/python3
"""
Module that returns true or false
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of a class
    that inherited(directly or indirectly) from the specified class if not
    return False
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
