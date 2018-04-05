"""

C(n,k) = C(n-1,k-1) + C(n-1,k)
C(n,n) = C(n,0) = 1 (empty set)

"""
from functools import lru_cache
import sys

sys.setrecursionlimit(20000)

#@lru_cache(maxsize=None)
cache = {}

def binomialCoeff(n, k):
    key = (n, k)
    if key in cache:
        return cache[(n, k)]
    if k == 0 or n == k:
        return 1
    cache[key] = binomialCoeff(n-1, k-1) + binomialCoeff(n-1, k)
    return cache[key]
# we observe that same subproblemes are repeatedly solved during the recursive steps

# re-computation of same subproblems can be avoided by constructing a temporary array C[][] in bottom-up manner
def binomialCoeffBottomUp(n, k):
    C = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                C[i][j] = 1

            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C[n][k]

n = 4000
k = 100
print("C(n,k) =",binomialCoeffBottomUp(n,k))
print("C(n,k) =",binomialCoeff(n,k))

