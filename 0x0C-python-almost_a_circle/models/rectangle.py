#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """the functions for the Rectangle class goes here"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes a new Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
