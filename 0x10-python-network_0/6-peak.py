#!/usr/bin/python3
# function that finds a peak in a list of unsorted integers.

def find_peak(list_of_integers):
    """returns peak value"""
    if type(list_of_integers) != list:
        return
    if list_of_integers:
        tmp = list_of_integers
        tmp.sort()
        return tmp[-1]
    else:
        return
