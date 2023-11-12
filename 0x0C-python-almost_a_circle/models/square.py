#!/usr/bin/python3
"""
    class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            initializing square class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            size setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
            str formatt
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """
            returns the dictionary representation of a Square
        """
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }

    def update(self, *args, **kwargs):
        """
            public method that assigns attributes
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
