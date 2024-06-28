#!/usr/bin/python3
""" Create a function that returns a list of integers"""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for a in range(1, n):
        prev_row = triangle[i - 1]
        new_row = [1]

        for b in range(1, a):
            new_row.append(prew_row[b - 1] + prev_row[b])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
