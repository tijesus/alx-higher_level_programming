#!/usr/bin/python3
"""Function to return Pascal's Triangle"""


def pascal_triangle(n):
    if n <= 0:
        return list()
    triangle = list()
    triangle.append([1])
    for i in range(1, n):
        row = list()
        row.append(1)
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
