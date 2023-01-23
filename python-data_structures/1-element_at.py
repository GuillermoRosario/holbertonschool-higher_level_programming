#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < len(my_list):
        return None
    elif idx == 0:
        return len(my_list)
    elif idx > len(my_list):
        return None
    print("Element at index {:d} is {}".format(idx, my_list))
