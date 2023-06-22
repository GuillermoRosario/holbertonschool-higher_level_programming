#!/usr/bin/python3
""" Create a Class"""


class BaseGeometry:
    """Class Documentation"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates value
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
