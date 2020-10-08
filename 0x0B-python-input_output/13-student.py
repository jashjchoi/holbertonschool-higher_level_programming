#!/usr/bin/python3
"""
    13-student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public method to retrieve dictionary of Student instance
        """
        if not attrs:
            return self.__dict__
        return ({key: value for key, value in self.__dict__.items()
                if key in attrs})

    def reload_from_json(self, json):
        """public method to replace attributes of Student instance"""
        self.__dict__.update(json)
