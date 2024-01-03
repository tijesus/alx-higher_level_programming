#!/usr/bin/python3
for i in reversed(range(65, 91)):
    """ assigning 32 to lower if the condition is met"""
    lower = 32 if (i % 2 == 0) else 0
    print("{}".format(chr(i + lower)), end="")
    