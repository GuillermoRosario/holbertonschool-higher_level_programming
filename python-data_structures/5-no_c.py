#!/usr/bin/python3
def no_c(my_string):

    my_new_string = my_string.translate({ord(C): None for i in 'c'})
    
    print(my_new_string)
