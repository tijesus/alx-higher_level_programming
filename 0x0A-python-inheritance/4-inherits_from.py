#!/usr/bin/python3
"""function to check subclass of an object"""


def inherits_from(obj, a_class):
    """can also return true on subclass of an object"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
