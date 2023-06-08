#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    new_list = list(my_list)
    length = len(my_list) - 1

    if idx > length or idx < 0:
        return new_list

    new_list[idx] = element

    return new_list
