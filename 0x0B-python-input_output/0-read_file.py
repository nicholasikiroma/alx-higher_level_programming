#!/usr/bin/python3

"""This module contains the function read_file"""


def read_file(filename=""):
    with open('filename', encoding='utf-8') as a_file:
        return a_file.read()
