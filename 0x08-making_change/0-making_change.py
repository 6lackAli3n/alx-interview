#!/usr/bin/python3
"""
Change-making algorithm: Determine the fewest
number of coins needed
to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coin
    needed to meet the total.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0
    remaining_total = total

    for coin in coins:
        if remaining_total <= 0:
            break
        count = remaining_total // coin
        num_coins += count
        remaining_total -= count * coin

        if remaining_total == 0:
            return num_coins
        else:
            return -1
