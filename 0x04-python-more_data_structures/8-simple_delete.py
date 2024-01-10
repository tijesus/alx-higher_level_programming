#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for _key in sorted(a_dictionary.keys()):
        if _key == key:
            del(a_dictionary[_key])
            return (a_dictionary)
    del(a_dictionary[key])
    return a_dictionary
