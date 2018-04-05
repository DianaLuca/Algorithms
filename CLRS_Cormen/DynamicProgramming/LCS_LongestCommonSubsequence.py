"""
In the longest-common-subsequence problem, we are given two sequences 
X = {x1; x2; :::; xmi } and Y = {y1; y2; :::; yni} and wish to find a maximum-length common subsequence of X and Y . 
This section shows how to efficiently solve the LCS problem using dynamic programming.

SUBSEQUENCE <in order but not necessary continuous> ex: given the string "abcd" has as subsequence the string "acd"

In a brute-force approach to solving the LCS problem, we would enumerate all subsequences of X 
and check each subsequence to see whether it is also a subsequence of Y , keeping track of the longest subsequence we find. 
Each subsequence of X corresponds to a subset of the indices f1;2;:::;mg of X. 
Because X has 2**m subsequences, this approach requires exponential time, making it impractical for long sequences.

"""


def LCS(x, y):
    n = len(x)
    m = len(y)
    C = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if x[i] == y[j]:
                C[i + 1][j + 1] = C[i][j] + 1
            else:
                C[i + 1][j + 1] = max(C[i][j + 1],C[i + 1][j])
    for i in range(n+1):
        for j in range(m+1):
            print(C[i][j], end=", ")
        print()
    return C[n][m]

X = [1,0,0,1,0,1,0,1]
Y = [0,1,0,1,1,0,1,1,0]
print(LCS(X,Y))
# it might be [1,0,1,0,1,0] or [1,0,1,1,0,1] both subsequences of length 6