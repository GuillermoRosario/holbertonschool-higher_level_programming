#!/usr/bin/python3
"""
This module contains a child class
named MyList that inherits from list
"""


class MyList(list):
    """
    This class inherits from a list
    """
    def print_sorted(self):
        """
        Print a sorted list
        in ascending order
        """
        my_list = []
        for num in self:
            my_list.append(num)
        my_list.sort()
        print(my_list)
