#!/usr/bin/python3
"""
This is the Declaration of a Function that
if object passed is instance the class is passed
"""


def is_kind_of_class(obj, a_class):
    """
    Returns true in Obj is an instance
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
