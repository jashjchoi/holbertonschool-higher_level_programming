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

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dum = cls(1, 1)
        if cls.__name__ == "Square":
            dum = cls(1, 1)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """adding the class method that returns a list of instances"""
        try:
            with open(cls.__name__ +".json", "r", encoding="UTF-8") as f:
                tmp = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in tmp]
