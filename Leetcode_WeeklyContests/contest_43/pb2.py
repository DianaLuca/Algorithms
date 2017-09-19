from fractions import gcd


class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0

        if n == 2 or n == 3 or n == 4 or n == 5:
            return n

        gc = gcd(n, n)
        j = n
        while gc <= j:
            j -= 1
            gc = gcd(n, j)

        return n // gc + self.minSteps(gc)