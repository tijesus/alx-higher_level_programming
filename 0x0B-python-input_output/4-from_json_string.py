#!/usr/bin/python3
"""function that returs object(string) representation JSON
    an object
"""
import json


def from_json_string(my_str):
    """returns object representation JSON"""
    return json.loads(my_str)
