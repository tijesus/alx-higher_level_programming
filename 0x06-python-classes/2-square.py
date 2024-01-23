#!/usr/bin/python3
"""class of a square"""


class Square:
    """class that define square"""
    def __init__(self, size=0):
        """Validating the size for the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
