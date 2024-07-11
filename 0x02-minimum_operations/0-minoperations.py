#!/usr/bin/python3
""" Method that calculates the fewest number of operations"""


def minOperations(n):
    """ prototype for calculations"""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
