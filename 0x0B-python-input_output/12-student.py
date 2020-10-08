#!/usr/bin/python3
"""
    12-student
"""


class Student:
    """class Student that defines a student by
       public instance attr
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method to retrieve dictionary of Student instance
        """
        if not attrs:
            return self.__dict__
        return ({key: value for key, value in self.__dict__.items()
                if key in attrs})
