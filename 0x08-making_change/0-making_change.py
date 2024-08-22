#!/usr/bin/python3
""" Given a pile of coins of different values, determine the fewest
    number of coins needed """


def makeChange(coins, total):
    """ Function to determine the total number of coins needed """
    if total <= 0:
        return 0
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0
    for coin in coins:
        for x in range(coin, total + 1):
            if x >= coin:
                min_coins[x] = min(min_coins[x], min_coins[x - coin] + 1)
    if min_coins[total] != float('inf'):
        return min_coins[total]
    else:
        return -1
