#!/usr/bin/python3
"""
Create a class named 'Rectangle'
that inherits from base
"""
from models.base import Base


class Rectangle(Base):
    """
    Class that defines a Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize and assign the value to representations
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width
    
    @width.setter
    def width(self, width):
        """Sets the width of the rectangle"""
        self.__width = width

    @property
    def height(self):
        """Return the height of the rectangle"""
        return self.__height
    
    @height.setter
    def height(self, height):
        """Sets the height of the Rectangle"""
        self.__height = height

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
