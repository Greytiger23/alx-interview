#!/usr/bin/python3
""" Function that determines winner of the game based on different values of n
    then returns the player with the most wins. """


def isWinner(x, nums):
    """ determines winner of the game and shows result """
    if not nums or x < 1:
        return None

    max_num = max(nums)

    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, max_num + 1, i):
                primes[multiple] = False

    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
