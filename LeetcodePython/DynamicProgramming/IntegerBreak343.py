"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. 
Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).
Note: You may assume that n is not less than 2 and not larger than 58.
"""


class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n - 1 ways to cut n
        # n = 1 + (n-1) = 2 + (n - 2) = 3 + (n - 3) ...... = (n - 1) + 1

        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = i

        for i in range(4, n + 1):
            for j in range(1, i):
                print("Try to split {} in {} and {}".format(i, i - j, j))
                dp[i] = max(dp[i], dp[i - j] * dp[j])

        return dp[n]

