#!/usr/bin/python3
#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list

    List = len(my_list) - 1

    if idx > List:
        return my_list

    my_list[idx] = element

    return my_list
