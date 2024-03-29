#!/usr/bin/python3
"""class for a square"""


class Square:
    """class to handle square"""
    def __init__(self, size=0):
        """validating the size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """taking the area of the square"""
        return self.__size ** 2
