#!/usr/bin/python3
"""function to check the subclass of an object"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
