#!/usr/bin/python3
def no_c(my_string):
    rep_lace = ""
    for i in my_string:
        if i != 'c' or i != 'C':
            rep_lace += i
    return rep_lace
