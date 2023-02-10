#!/usr/bin/python3
"""
This module has a class called Rectangle that
is a child of BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """
    Recangle is a child class from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Method that validates height and width
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
