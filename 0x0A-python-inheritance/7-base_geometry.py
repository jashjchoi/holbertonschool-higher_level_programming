#!/usr/bin/python3
"""
   7-base_geometry.py module
"""


class BaseGeometry:
    """class BaseGeometry based on 6-base_geometry"""

    def area(self):
        """Public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
