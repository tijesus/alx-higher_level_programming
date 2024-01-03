#!/usr/bin/python3
def print_last_digit(number):
    numb = abs(number) % 10
    if number < 0:
        print("{}".format(numb), end="")
    else:
        print("{}".format(numb), end="")
    return numb
