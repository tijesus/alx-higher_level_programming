#!/usr/bin/python3
"""load, add and save command from command line"""


import sys

if __name__ == "__main__":
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    try:
        add_in = load('add_item.json')
    except FileNotFoundError:
        add_in = []

    add_in.extend(sys.argv[1:])
    save(add_in, "add_item.json")
