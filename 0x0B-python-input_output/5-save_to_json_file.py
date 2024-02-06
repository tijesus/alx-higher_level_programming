#!/usr/bin/python3
"""Function to save opject in a file"""
import json


def save_to_json_file(my_obj, filename):
    """Save to json file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
