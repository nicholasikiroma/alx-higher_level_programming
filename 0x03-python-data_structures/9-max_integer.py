#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        new_list = my_list[::]
        new_list.sort()
        return new_list[-1]
    else:
        return None
