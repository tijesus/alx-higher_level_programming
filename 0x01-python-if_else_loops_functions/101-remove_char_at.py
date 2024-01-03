#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return (str)
    """ use string slicing to get the number to remove and jump to next"""
    return (str[:n] + str[n+1:])
