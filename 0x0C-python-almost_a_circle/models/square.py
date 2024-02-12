#!/usr/bin/python3
"""Class for Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """all square initialisation function goes here"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        if args:
            attr = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        dictionary = {"id": self.id, "size": self.size,
                       "x": self.x, "y":self.y}
        return dictionary

