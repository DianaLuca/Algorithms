# In combinatorial mathematics, a derangement is a permutation of the elements of a set,
# such that no element appears in its original position.
# There's originally an array consisting of n integers from 1 to n in ascending order,
# you need to find the number of derangement it can generate.
#
# Also, since the answer may be very large, you should return the output mod 10e9 + 7.
#
# Example 1:
# Input: 3
# Output: 2
# Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] and [3,1,2].
# Note:
# n is in the range of [1, 106].


class Solution(object):

    """ Dynamic programming approach:
    the recursive formula for finding the derangements for nn elements is given by:
    dp[i] = (i−1) * (dp[i−1] + dp[i−2])
    O(n) time, O(n) space
    
    """
    def findDerangement_dynamic_programming(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 0

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 0
        for i in range(2, n+1):
            dp[i] = ((i-1) * (dp[i-1] + dp[i-2])) % 1000000007

        return dp[n]

    def findDerangement_math_formula(self, n):
        """
        :type n: int
        :rtype: int
        Using mathematical formula approach: 
        O(n) time, O(1) space
        """
        mul = 1
        summ = 0
        M = 1000000007
        for i in reversed(range(n + 1)):
            summ = (summ + M + mul * (1 if i % 2 == 0 else -1)) % M
            mul = (mul * i) % M

        return summ
