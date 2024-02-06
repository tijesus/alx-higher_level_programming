#!/usr/bin/python3
"""function that returns dictionary discreption with 
    siple data sructure
"""


def class_to_json(obj):
    """returns dictionary description of JSON
        you can just return obj.__dict__    
    """
    new_json = {}
    #__dict__.item() is a built in method to check the items of a dictionary
    for name, value in obj.__dict__.items():
        if isinstance(value, (list, str, bool, int, dict)):
            new_json[name] = value
        else:
            pass
    return new_json
