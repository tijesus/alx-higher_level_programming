#!/usr/bin/python3
"""function that returs JSONrepresentation of
    an object(string)
"""
import json


def to_json_string(my_obj):
    """returns JSON representation of object"""
    return json.dumps(my_obj)
