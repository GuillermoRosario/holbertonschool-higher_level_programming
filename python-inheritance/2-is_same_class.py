#!/usr/bin/python3


"""Defines main Function"""


def is_same_class(obj, a_class):

    """Variable declaration and Condition"""

    if a_class != bool:
        if obj is True or obj is False:
            return False
    if a_class != object:
        if isinstance(obj, a_class):
            return True
        else:
            return False
    else:
        return False
