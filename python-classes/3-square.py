#!/usr/bin/python3
"""Creation of an empty class defining a Square"""


class Square:
    """Write an empty class square that defines a square"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        self = self.__size * self.__size
        return self
    