# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.

class Solution(object):
    def trailingZeroesIterative(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        cnt = 0
        while n > 0:
            cnt += n//5
            n //= 5

        return cnt

    def trailingZeroesRecursive(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        return n / 5 + self.trailingZeroesRecursive(n / 5)