#!/usr/bin/python3

"""Module contains the from_json_string function"""


import json


def from_json_string(my_str):
    """function that returns a python object from a JSON string"""
    return json.loads(my_str)
