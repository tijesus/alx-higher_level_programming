#!/usr/bin/python3
"""Evaluate  Rectangle"""


class Rectangle:
    """Class to Evaluate Rectangle"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (2 * self.__height)

    def __str__(self) -> str:
        if self.__width == 0 or self.__height == 0:
            return ("")
        output = ""
        for i in range(self.__height):
            for j in range(self.__width):
                output += "#"
            if i < self.__height - 1:
                output += "\n"
        return output

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
