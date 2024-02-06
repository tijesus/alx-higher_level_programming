#!/usr/bin/python3
"""Class that inherits from square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """creating rectangle class"""

    def __init__(self, size):
        """initializes a square function"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
