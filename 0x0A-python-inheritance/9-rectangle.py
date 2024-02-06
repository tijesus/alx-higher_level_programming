#!/usr/bin/python3
"""class that raises error when empty"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this inherits from base geometry"""

    def __init__(self, width, height):
        """function to initialise the inheritancey"""
        # super().__init__(width, height)s
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """funcion to return area"""
        return self.__width * self.__height

    def __str__(self):
        """function to print"""
        return "[Rectangele]{}/{}".format(self.__width, self.__height)
