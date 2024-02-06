#!/usr/bin/python3
"""Function that reads test files and print 
    to stdout
"""

def read_file(filename=""):
    """Reads test files and prints"""
    with open(filename) as f:
        for line in f:
            print(line, end="")
