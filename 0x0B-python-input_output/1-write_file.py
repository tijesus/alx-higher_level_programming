#!/usr/bin/python3
"""writing into a text file"""


def write_file(filename="", text=""):
    """write a text file"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
