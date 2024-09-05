#!/usr/bin/python3
""" Function that determines winner of the game based on different values of n
    then returns the player with the most wins. """

def isWinner(x, nums):
    """ determines winner of the game and shows result """
    if not nums or x <= 0:
        return None

    def prime_game(n):
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0], is_prime[1] = False, False
        return [i for i in range(n + 1) if is_prime[i]]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = prime_game(n)
        if not primes:
            ben_wins += 1
            continue

        moves = 0
        for prime in primes:
            moves += 1
            multiples = list(range(prime, n + 1, prime))
            for m in multiples:
                if m in primes:
                    primes.remove(m)

        if moves % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
