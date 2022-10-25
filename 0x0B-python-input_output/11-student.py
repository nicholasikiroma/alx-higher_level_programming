#!/usr/bin/python3

"""Defines a class Student"""


class Student:
    """Models a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation of class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for i in attrs:
            try:
                new_dict[i] = self.__dict__[i]
            except:
                pass
        return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except:
                pass
