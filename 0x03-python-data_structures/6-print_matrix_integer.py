#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        space = ""
        for j in i:
            print("{}{:d}".format(space, j), end="")
            space = " "
        print('')
