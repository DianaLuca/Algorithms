"""
The problem of cutting a rod into rods of smaller length in way that maximizes their total value.

Given a rod of length n inches and a table of prices pi for i D 1; 2; : : : ; n, 
determine the maximum revenue rn obtain- able by cutting up the rod and selling the pieces. 
Note that if the price pn for a rod of length n is large enough, an optimal solution may require no cutting at all.

We can cut up a rod of length n in 2n 1 different ways, since we have an independent option of cutting, 
or not cutting, at distance i inches from the left end,
lengthi 1 2 3 4 5 6 7 8 9 10 
pricepi 1 5 8 9 10 17 17 20 24 30
"""

import sys


#top down recursive solution: nonoptimal
#running time is exponential in n: T(n) = 2**n
def cut_rod_recursive(p, n):
    """
    :param p: list of prices
    :param n: length of rod
    :example: p = [1 5 8 9 10 17 17 20 24 30]
    :return: maximum obtained value
    """
    if n == 0:
        return 0
    res = -sys.maxsize
    for i in range(n):
        res = max(res, p[i] + cut_rod_recursive(p, n-i-1))
    return res


"""
Using Dynamic Programming:
1: Top-Down with memoization <recording a value so that we can look it up later>
2: Bottom-Up Method
"""


def memoized_cut_rod(p, n):
    r = [-sys.maxsize for _ in range(n)]
    return _memoized_cut_rod(p, n, r)


def _memoized_cut_rod(p, n, r):
    if r[n-1] >= 0:
        return r[n-1]
    if n == 0:
        return 0
    res = 0
    for i in range(n):
        res = max(res, p[i] + _memoized_cut_rod(p,n-i-1,r))
    r[n-1] = res
    return res


def bottom_up_cut_rod(p, n):
    dp = [0 for _ in range(n + 1)]

    for j in range(1, n + 1):
        res = -sys.maxsize

        for i in range(1, j+1):
            res = max(res, p[i-1]+dp[j-i])

        dp[j] = res
        print("dp[{}] = {}".format(j, dp[j]))

    return dp[n]


# tester : p = [1, 5, 8, 9, 10]
p = [1, 5, 8, 9, 10]
n = len(p)
print(cut_rod_recursive(p, n))
print(memoized_cut_rod(p,n))
print(bottom_up_cut_rod(p,n))