# Multiply two matrices: Cubic time complexity O(n^3)


def multiply_matrix(a, b, n):

    # How to initialize a matrix: #rows x #cols (with 0es):
    # >> > matrix = [[[0] for _ in range(3)] for _ in range(3)]
    # >> > matrix
    # [[[0], [0], [0]], [[0], [0], [0]], [[0], [0], [0]]]
    # >> > matrix = [[0] * 3 for _ in range(3)]
    # >> > matrix
    # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # >> >
    c = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]

            print('C[{},{}] = {}'.format(i, j, c[i][j]))

A = [[2, 2], [2, 2]]
B = [[1, 2], [3, 4]]
multiply_matrix(A, B, 2)