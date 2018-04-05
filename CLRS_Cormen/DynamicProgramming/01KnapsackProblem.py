"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. 
Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that 
sum of the weights of this subset is smaller than or equal to W. You cannot break an item, 
either pick the complete item, or don’t pick it (0-1 property).
"""

def print_mx(dp):
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            print(dp[i][j],end='\t')
        print()


def oIknapsack(val, wt, W):
    n = len(val)

    dp = [[0 for _ in range(W + 1)] for _ in range(n+1)]
    print(dp)
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    print_mx(dp)
    return dp[n][W]


# test case
val = [60, 100, 120]
wt = [1, 2, 3]
W = 5
# solution = 220
solution = oIknapsack(val, wt, W)
print(solution)