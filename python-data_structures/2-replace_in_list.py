#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
 
    List = len(my_list)
    if idx < 0 or idx > List - 1:
        return my_list
    my_list[idx] = element
    print(my_list)
