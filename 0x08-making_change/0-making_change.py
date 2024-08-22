#!/usr/bin/python3
""" Given a pile of coins of different values, determine the fewest
    number of coins needed """


def makeChange(coins, total):
    """ Function to determine the total number of coins needed """
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for x in range(1, total + 1):
        for coin in coins:
            if coin <= x:
                min_coins[x] = min(min_coins[x], min_coins[x - coin] + 1)

    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]
