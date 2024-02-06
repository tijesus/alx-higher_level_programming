#!/usr/bin/python3
"""Function that creates an object from JSON file"""
import json


def load_from_json_file(filename):
    """Loads a object from JSON file"""
    """could also return json.loads(json_file)"""
    with open(filename, 'r') as json_file:
        temp = json.loads(json_file.read())
    return temp
