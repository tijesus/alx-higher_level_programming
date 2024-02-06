#!/usr/bin/python3
"""function that returs object(string) representation JSON
    an object
"""
import json


def to_json_string(my_obj):
    """returns object representation JSON"""
    return json.loads(my_obj)
