#!/usr/bin/python3
"""function that returns dictionary discreption with 
    siple data sructure
"""


def class_to_json(obj):
    return obj.__dict__
