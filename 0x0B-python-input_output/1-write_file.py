#!/usr/bin/python3

"""This module contains write_file function"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)

    Returns: number of characters written
    """
    with open(filename, 'w', encoding='uft-8') as a_file:
        return a_file.write(text)
