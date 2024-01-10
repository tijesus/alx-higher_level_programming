#!/usr/bin/python3
def uniq_add(my_list=[]):
    init = 0
    for i in set(my_list):
        init = init + i
    return init
