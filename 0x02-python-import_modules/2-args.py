#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv) -1

    if argc == 0:
        print("0 argument")
    elif argc == 1:
        print("1 arguement:")
    else:
        print("{} arguments".format(argc))
    for i in range(argc):
        print("{}: {}".format( i + 1, argv[i + 1]))

