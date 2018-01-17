""" This algorithm takes: O(n^3)
Strassen’s remarkable recursive algorithm for multiplying nxn matrices. It runs in n^lg7 time. Since lg 7 lies between 2:80 and 2:81, 
Strassen’s algorithm runs in n^2,81 time, which is asymptotically better than the simple SQUARE-MATRIX- MULTIPLY procedure
"""


def square_matrix_multiply(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(square_matrix_multiply(A, B))

"""
matrix addition or subtraction, O(n^2)
"""