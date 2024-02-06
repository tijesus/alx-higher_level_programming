#!/usr/bin/python3
"""class that raises error when empty"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this inherits from base geometry"""

    def __init__(self, width, height):
        """function to initialise the inheritancey"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
