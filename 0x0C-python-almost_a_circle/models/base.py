#!/usr/bin/python3
"""Base class for the model"""


import json


class Base():
    """class initialising the base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialise the base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a json string representation of a list of dictionaries"""
        if list_dictionaries == [] or \
                list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json representation of file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                l_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(l_dicts))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                dummy = cls(1)
            elif cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'
        try:
            with open(cls.__name__ + ".json", "r") as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**dic) for dic in list_dicts]
        except FileNotFoundError:
            return []
