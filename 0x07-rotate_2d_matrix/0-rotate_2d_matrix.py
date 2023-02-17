#!/usr/bin/python3
""" 0. Rotate 2D Matrix
Working algorithm
--------
1) original matrix

1 2 3
4 5 6
7 8 9

2) transpose

1 4 7
2 5 8
3 6 9

3-a) change rows to rotate left
- change rows' means 'flip row 0 with row n, row 1 with row n-1, etc

3 6 9
2 5 8
1 4 7

3-b) or change columns to rotate right
- change columns' means 'flip row 0 with row n, row 1 with row n-1, etc

7 4 1
8 5 2
9 6 3
"""


def rotate_2d_matrix(matrix):
    """ in-place rotates a n x n matrix 90 degrees clockwise. """
    # in-place transpose matrix
    if type(matrix) is not list:
        return
    if not matrix:
        return
    if not all(type(row) is list for row in matrix):
        return
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # flip columns
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - j - 1] = \
                matrix[i][n - j - 1], matrix[i][j]
