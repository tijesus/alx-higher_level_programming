#!/usr/bin/python3
"""class that raises error when empty"""


class BaseGeometry(object):
    """raise w=error when function not set"""
    def area(self):
        raise Exception("area() is not implemented")
