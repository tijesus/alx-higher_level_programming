#!/usr/bin/python3
"""Append into a text file"""


def append_write(filename="", text=""):
    """Append a text file"""
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
