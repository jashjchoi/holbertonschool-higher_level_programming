#!/usr/bin/python3
"""file for task 5"""


class Square:
    """define class Square with print method"""
    def __init__(self, size=0):
        """init method"""
        self.size = size

    @property
    def size(self):
        """retreive size getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method to validate value"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """returns square area"""
        return (self.__size**2)

    def my_print(self):
        """prints in stdout square with character #"""
        if self.__size is 0:
            print()

        for row in range(self.__size):
            for col in range(self.__size):
                print('{}'.format('#'), end="")
            print()
