#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    av = sys.argv
    ac = len(av)
    sum = 0

    for i in range(1, ac):
        result = av[i]
        sum = int(sum) + int(result)
    print("{:d}".format(sum))
