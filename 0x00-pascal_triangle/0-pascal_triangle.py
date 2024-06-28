#!/usr/bin/python3
""" Create a function that returns a list of integers"""


def pascal_triangle(n):
    """ returns a list of lists of integers """
    if n <= 0:
        return []

    triangle = [[1 for _ in range(a + 1)] for a in range(n)]
    for a in range(2, n):
        for b in range(1, a):
            triangle[a][b] = triangle[a - 1][b - 1] + triangle[a - 1][b]

    return triangle
