#!/usr/bin/python3
"""square.py"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """returns formatted info method of square
        """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def update(self, *args, **kwargs):
        """update class Square by adding the public method"""
        if args:
            updatesq = ['id', 'size', 'x', 'y']
            j = 0
            for arg in args:
                setattr(self, updatesq[j], arg)
                j += 1
            return
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return dictionary representation of class Square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
