#!/usr/bin/python3

"""module contains append_write function"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text"""
    with open(filename, 'a', encoding='utf-8') as a_file:
        return a_file.write(text)
