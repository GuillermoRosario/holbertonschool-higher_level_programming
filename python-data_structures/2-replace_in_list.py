#!/usr/bin/python3

def replace_in_list(my_list, idx, element):


    List = len(my_list)

    if idx < 0 or idx > List:
        return my_list
    if idx > 0 or idx < List:
        my_list[idx] = element
        return my_list
