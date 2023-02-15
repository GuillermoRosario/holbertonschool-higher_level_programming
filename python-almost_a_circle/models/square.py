#!/usr/bin/python3
"""
Create a class named Square
that inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Inherited Class receiving size, x, y, and id
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Validates super class attributes
        and assigns them
        """
        super().__init__(size, size, x, y, id)

    """
    Property Getters and Setters
    """

    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value


    def __str__(self):
        """
        String Rep of the Square Object
        Returns [Square] (<id>) <x>/<y> - <size>
        size = width and height
        """
        return (f'[Square] ({self.id}) {self.x}/{self.y} - '
                f'{self.width}')

    def update(self, *args, **kwargs):
        """
        Class that updates the attributes
        of a square Object
        """
        argument = 0
        if args is not None:
            for attribute in args:
                if argument == 0:
                    self.id = attribute
                elif argument == 1:
                    (super(__class__, self.__class__)
                        .width.__set__(self, attribute))
                elif argument == 2:
                    (super(__class__, self.__class__)
                        .x.__set__(self, attribute))
                elif argument == 3:
                    (super(__class__, self.__class__)
                        .y.__set__(self, attribute))
                argument += 1

        for key in kwargs:
            if key == "id":
                self.id = kwargs.get(key)
            elif key == "size":
                (super(__class__, self.__class__)
                    .width.__set__(self, kwargs.get(key)))
            elif key == "x":
                (super(__class__, self.__class__)
                    .x.__set__(self, kwargs.get(key)))
            elif key == "y":
                (super(__class__, self.__class__)
                    .y.__set__(self, kwargs.get(key)))
                    
    def to_dictionary(self):
        """Return dictionary representation of the Rectangle."""
        sqr_dict = {}
        sqr_dict['id'] = self.id
        sqr_dict['size'] = self.size
        sqr_dict['x'] = self.x
        sqr_dict['y'] = self.y
        return sqr_dict