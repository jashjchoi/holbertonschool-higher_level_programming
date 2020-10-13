#!/usr/bin/python3
"""
    base.py module
"""
import json


class Base:
    """ Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of str (list of dict)
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write an object to a text file using a JSON"""
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string([i.to_dictionary() for i
                        in list_objs]))

    @staticmethod
    def from_json_string(list_dictionaries):
        """returns a str dict list represented by a JSON"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.loads(list_dictionaries)
