#!/usr/bin/python3
"""class for student"""


class Student:
    """class to define student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """check if attrs is a list
            iterate through atter to check if all attributes are string
            iterate the attrs and use hasattr to check if attribute exist
            if it exist, new dictionary is created and
            getattr gets it and return its key and value
        """
        if isinstance(attrs, list) and\
            all(isinstance(x, str) for x in attrs):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        else:
            return self.__dict__

