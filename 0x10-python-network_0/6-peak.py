#!/usr/bin/python3
"""Moddule contains a function that finds the peak value of a list"""


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
