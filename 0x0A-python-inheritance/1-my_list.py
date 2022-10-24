#!/usr/bin/python3
"""contains the MyList class"""


class MyList(list):
    """derieved class of list"""
    def __init__(self):
        """initialises the object"""
        super().__init_()

    def print_sorted(self):
        """prints list in ascending order"""
        print(sorted(self))
