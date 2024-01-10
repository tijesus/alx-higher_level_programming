#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for _key in sorted(a_dictionary.keys()):
        if _key == key:
            a_dictionary[_key] = value
            return (a_dictionary)
    a_dictionary[key] = value
    return a_dictionary


