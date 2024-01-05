#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys

    av = sys.argv
    ac = len(av)
    if  ac - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    """ creating a dictionary with key and value pairs """    
    opera = {'+': add, '-': sub, '*': mul, '/': div}
 
    if av[2] not in list(opera.keys()):
        print("Unknown operator. Available operators: +, -, * and / ")
        sys.exit(1)
    a = int(av[1])
    b = int(av[3])
    print("{} {} {} = {}".format(a, av[2], b, opera[av[2]](a, b)))
