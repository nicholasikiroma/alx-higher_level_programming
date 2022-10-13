#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    tmp = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            tmp += 1
    except IndexError:
        None
    print()
    return tmp
