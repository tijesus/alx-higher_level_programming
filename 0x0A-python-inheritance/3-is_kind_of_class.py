#!/usr/bin/python3
"""function to check the class and inheritance of an object"""


def is_kind_of_class(obj, a_class):
    """returns true if object is instance of class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
