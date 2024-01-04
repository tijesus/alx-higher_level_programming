#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    av = sys.argv
    ac = len(av) - 1
    if ac == 0:
        print("0 arguments.")
    elif ac == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(ac))
    for i in range(ac):
        print("{}: {}".format(i + 1, av[i + 1]))
