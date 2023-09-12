#!/usr/bin/python3
"""
This module contains a chils class names Square
that inherited from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square is a class from Rectangle
    """
    def __init__(self, size):
        """
        Initalizes square class by asigning the size
        """
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """
        Print Square Description
        """
        return f"[Square] {self.__size}/{self.__size}"
