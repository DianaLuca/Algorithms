# Given an integer, write a function to determine if it is a power of three.

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False

        tpow = 1
        while tpow < n:
            tpow *= 3

        if tpow == n:
            return True
        else:
            return False