#!/usr/bin/python3
"""Class that inherits from list class."""


class MyList(list):
    """the list that is to be inherited"""
    def print_sorted(self):
        print(sorted(self))
