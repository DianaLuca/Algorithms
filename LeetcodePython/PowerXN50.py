# Implement pow(x, n).

class Solution():
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if n < 0:
            x = 1/x
            n = -n

        if n % 2 == 0:
            return pow(x*x, n//2)
        else:
            return x * pow(x*x, n//2)