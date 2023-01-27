#!/usr/bin/python3
def uniq_add(my_list=[]):

        unique_list = set(my_list)
        unique_add = 0

        for number in unique_list:
            unique_add += number
        return(unique_add)
