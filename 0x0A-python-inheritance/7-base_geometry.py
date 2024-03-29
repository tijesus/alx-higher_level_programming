#!/usr/bin/python3
"""class that raises error when empty"""


class BaseGeometry:
    """this perform base geometry"""

    def area(self):
        """area method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value as an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
