# 0x08 - Making Change

## Overview

This directory contains a solution to the problem of determining the fewest number of coins needed to meet a given total. the solution leverages dynamic programming to efficiently compute the result.

## Problem statement

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total. If the total cannot be met by any number of coins in your possession, return `-1`.

### Function Prototype

```python
def makeChange(coins, total):
	"""
	Determine the fewest number of coins needed to meet a given total.
	:param coins: List of values of the coins in your possession.
	:param total: The total amount to meet.
	:return: Fewwest number of coins neede to meet the total, or -1 if it's not possible.
	"""
