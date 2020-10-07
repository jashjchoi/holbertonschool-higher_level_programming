#!/usr/bin/python3
"""
    8-base_geometry.py module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry class that inherits from 7-base_geometry"""

    def __init__(self, width, height):
        """init method"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
