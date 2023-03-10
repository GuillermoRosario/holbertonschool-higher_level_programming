#!/usr/bin/python3
"""
Create a class named 'Rectangle'
that inherits from base
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        """
        Initialize and assign the value to representations
        """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height
        if type(x) is not int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x
        if type(y) is not int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    def area(self):
        """
        Print area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """Display rectangle with a #"""
        for newline in range(self.__y):
            print()
        for hash in range(self.__height):
            print(' ' * self.__x, end="")
            print('#' * self.__width)

    def __str__(self):
        """Update the class Rectangle by overriding the __str__ method so
        that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return (f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - '
                f'{self.__width}/{self.__height}')

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        count = 0
        if args is not None:
            for attribute in args:
                if count == 0:
                    self.id = attribute
                elif count == 1:
                    self.__width = attribute
                elif count == 2:
                    self.__height = attribute
                elif count == 3:
                    self.__x = attribute
                elif count == 4:
                    self.__y = attribute
                count += 1

        for password in kwargs:
            if password == "id":
                self.id = kwargs.get(password)
            elif password == "width":
                self.__width = kwargs.get(password)
            elif password == "height":
                self.__height = kwargs.get(password)
            elif password == "x":
                self.__x = kwargs.get(password)
            elif password == "y":
                self.__y = kwargs.get(password)

    def to_dictionary(self):
        """Return dictionary representation of the Rectangle."""
        rectngl_dict = {}
        rectngl_dict['id'] = self.id
        rectngl_dict['width'] = self.width
        rectngl_dict['height'] = self.height
        rectngl_dict['x'] = self.x
        rectngl_dict['y'] = self.y
        return rectngl_dict
