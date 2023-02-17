# Rotate 2D Matrix
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

- Prototype: def rotate_2d_matrix(matrix):
- Do not return anything. The matrix must be edited in-place.
- You can assume the matrix will have 2 dimensions and will not be empty.

```bash
jessevhedden$ python3 -m doctest -v 0-rotate_2d_matrix_test.txt
Trying:
    rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix
Expecting nothing
ok
Trying:
    matrix = [[1, 2, 3],
        [4, 5, 6],
      [7, 8, 9]]
Expecting nothing
ok
Trying:
    rotate_2d_matrix(matrix)
Expecting nothing
ok
Trying:
    matrix
Expecting:
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
ok
1 items passed all tests:
   4 tests in 0-rotate_2d_matrix_test.txt
4 tests in 1 items.
4 passed and 0 failed.
Test passed.
jessevhedden$
```