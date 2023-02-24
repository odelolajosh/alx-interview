#!/usr/bin/python3
""" 0. Change comes from within """

def makeChange(coins, total):
    """Return a list of coins to make the total.

    Args:
        coins (list): A list of available coins.
        total (int): The total amount to make change for.

    Returns:
        int: the fewest number of coins needed to meet total.
    """
    # change count and current coin index
    change = 0
    index = 0
    # sort coins in descending order
    coins.sort(reverse=True)
    while total > 0:
        if index >= len(coins):
            return -1
        if coins[index] <= total:
            total -= coins[index]
            change += 1
        else:
            index += 1
    return change
