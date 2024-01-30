#!/usr/bin/python
"""Function to divide matrix."""


def matrix_divided(matrix, div):
    text = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == [] or (
        not all(isinstance(row, list) for row in matrix)
    ):
        raise TypeError(text)

    elements = []
    [elements.extend(row) for row in matrix]

    if not all(isinstance(num, (int, float)) for num in elements):
        raise TypeError(text)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
