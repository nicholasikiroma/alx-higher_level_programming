#!/usr/bin/python3

"""This module contains the function read_file"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r', encoding='utf-8') as a_file:
        print(a_file.read(), end="")
