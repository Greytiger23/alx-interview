#!/usr/bin/python3
""" Given a pile of coins of different values, determine the fewest
    number of coins needed """


def makeChange(coins, total):
    """ Function to determine the total number of coins needed """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
