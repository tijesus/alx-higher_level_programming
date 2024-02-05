#!/usr/bin/python3
"""function to check if an object is an instance of class"""


def is_same_class(obj, a_class):
    """can also return type(obj) == a_class easily"""
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
