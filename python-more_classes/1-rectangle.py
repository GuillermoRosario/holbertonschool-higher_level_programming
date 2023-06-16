#!/usr/bin/python3
"""
This Module is a Rectangle
"""
class Rectangle:
    pass

def __init__ (self, width=0, height=0):
    #Width Parameters
    if type(width) is not int:
        raise TypeError("width must be an integer")
    elif width < 0:
        raise ValueError("width must be >= 0")
    else:
        self.__width = width
    #Height Parameters
    if type(height) is not int:
            raise TypeError('height must be an integer')
    elif height < 0:
            raise ValueError('height must be >= 0')
    else:
         self.__height = height

    @property
    def width(self):
         return self.__width
    
    @width.setter 
    def width(self, value):
         if type(value) is not int:
              raise TypeError("width must be an integer")
         elif value < 0: 
              raise ValueError("width must be >= 0")
    
    @property 
    def height(self):
         return self.__width

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
    