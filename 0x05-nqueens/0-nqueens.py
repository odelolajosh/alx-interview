#!/usr/bin/python3
""" Solution to the N queens problem """
import sys


def queens(n, i=0, a=[], b=[], c=[]):
    """
    Args:
        n (int): size of the board
        i (int): row
        a (list): columns
        b (list): diagonal
        c (list): other diagonal
    Yields:
        list: solution in the form of a list of lists
    """
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from queens(n, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        yield [[i, j] for i, j in enumerate(a)]


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise ValueError("Usage: nqueens N")

        N = sys.argv[1]
        if not N.isdigit():
            raise TypeError("N must be a number")

        N = int(N)
        if N < 4:
            raise ValueError("N must be at least 4")

        for solution in queens(N):
            print(solution)
    except Exception as err:
        if hasattr(err, "message"):
            print(err.message)
        else:
            print(err)
        sys.exit(1)
