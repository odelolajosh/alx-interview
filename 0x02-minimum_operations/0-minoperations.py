#!/usr/bin/python3
"""
0. Minimum Operations
In a text file, there is a single character H.
Your text editor can execute only two operations in this
file: Copy All and Paste
"""


def minOperations(n):
    """calculates the fewest number of operations
    needed to result in exactly n 'H' characters in the file.
    """
    if n <= 1:
        return 0

    # first operation has to be copy and paste already
    operations = 2
    hs = 2
    clipboard = 1

    while hs < n:
        if (n - hs) % hs == 0:
            operations += 2
            clipboard = hs
        else:
            operations += 1

        hs += clipboard

    return operations
