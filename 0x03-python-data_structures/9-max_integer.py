#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    max = my_list[0]
    i = 0
    while i < len(my_list):
        if my_list[i] > max:
            max = my_list[i]
    i += 1
    return max
