#!/usr/bin/python3
"""class that raises error when empty"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """function to initialise the inheritancey"""

    def __init__(self, width, height):
        """initialse the inheritance"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate the Rectagle's area"""
        return self.__width * self.__height

    def __str__(self):
        """Return description of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
