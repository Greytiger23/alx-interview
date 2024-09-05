# Prime Game

## Description

This project implements a prime number game between two players, Maria and Ben. Given a set of consecutive integers starting from 1 up to and including `n`, Maria and Ben take turns picking prime numbers and removing the prime number and all its multiples from the set. The player who cannot make a move loses the game. Maria always plays first, and both players play optimally.

The program determines the winner of multiple rounds of the game based on different values of `n`, then returns the player with the most wins.

## Prototype

```python
def isWinner(x, nums)
