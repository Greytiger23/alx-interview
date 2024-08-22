#!/usr/bin/python3
""" Given a pile of coins of different values, determine the fewest
    number of coins needed """


def makeChange(coins, total):
    """ Function to determine the total number of coins needed """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total == 0:
            break
        count += total // coin
        total %= coin

    if total == 0:
        return count
    else:
        return -1
