# Given a non-negative integer c, your task is to decide
# whether there're two integers a and b such that a2 + b2 = c.
#
# Example 1:
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:
# Input: 3
# Output: False

from math import sqrt


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(0, int(sqrt(c)) + 1):
            rem = c - a ** 2
            if rem >= 0:
                b = int(sqrt(rem))
                if b ** 2 == rem or (b + 1) ** 2 == rem:
                    return True

        return False

s = Solution()
print(s.judgeSquareSum(0))  # true
print(s.judgeSquareSum(1))  # true
print(s.judgeSquareSum(3))  # false
