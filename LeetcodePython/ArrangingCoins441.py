# You have a total of n coins that you want to form in a staircase shape,
# where every k-th row must have exactly k coins.
# Given n, find the total number of full staircase rows that can be formed.
# n is a non-negative integer and fits within the range of a 32-bit signed integer.


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n

        while l <= r:

            m = l + (r - l) // 2
            res = m * (m + 1) // 2

            if res <= n:
                l = m + 1
            else:
                r = m - 1
        return l - 1
