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

   def __str__(self):
        """
        String Rep of the Square Object
        Returns [Square] (<id>) <x>/<y> - <size>
        size = width and height
        """
        return (f'[Square] ({self.id}) {self.x}/{self.y} - '
                f'{self.__width}')
