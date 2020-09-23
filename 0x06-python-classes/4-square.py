#!/usr/bin/python3
"""file for task 4"""


class Square:
    """define Class Square with getter and setter"""

    def __init__(self, size=0):
        """initiate method"""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method to initalize value"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """returns current square area"""
        return (self.__size**2)
