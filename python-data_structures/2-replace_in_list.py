#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5]
idx = 3
element = 9

def replace_in_list(my_list, idx, element):
    List = len(my_list)
    if idx < 0 or idx > List:
        return my_list
    my_list[idx] = element
    print(my_list)
