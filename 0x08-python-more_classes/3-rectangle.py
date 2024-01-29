#!/usr/bin/python3
"""String Rectangle"""


class Rectangle:
    """Class returning a string representation of rectangle"""
    def __init__(self, width=0, height=0):
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
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
    
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        output = ""
        for i in range(self.__height):
            for j in range(self.__width):
                output += "#"
            if i < self.__height - 1:
                output += "\n"
        return output
