# Implement int sqrt(int x).
# Compute and return the square root of x.


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: float
        :rtype: float
        """
        l, r = 0, x

        while l + 1e-6 <= r:
            print(l, r)
            m = l + (r - l)/2
            if m**2 <= x:
                l = m
            else:
                r = m
        return l

s = Solution()
r = s.mySqrt(81)
print(r)