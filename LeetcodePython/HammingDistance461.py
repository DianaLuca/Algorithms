# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.
# Note:
# 0 ≤ x, y < 231.

class Solution(object):
    def hammingDistanceOneLine(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # xor, count
        return bin(x ^ y).count('1')

    def hammingPisoi(self, x, y):
        result = 0
        for i in range(12):
            bitx = (x & (1<<i)) >> i
            bity = (y & (1<<i)) >> i
            result += abs(bitx - bity)
        return result

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        binx = bin(x)
        biny = bin(y)
        xlen = len(binx)
        ylen = len(biny)
        cnt = 0

        if xlen == ylen:
            for i in reversed(range(2, xlen)):
                if binx[i] != biny[i]:
                    cnt += 1

        elif xlen < ylen:
            d = ylen - xlen
            for i in reversed(range(2, xlen)):
                if binx[i] != biny[i + d]:
                    cnt += 1
            cnt += biny[2:d + 2].count('1')

        elif xlen > ylen:
            d = xlen - ylen
            for i in reversed(range(2, ylen)):
                if binx[i + d] != biny[i]:
                    cnt += 1
            cnt += binx[2:d + 2].count('1')

        return cnt


print(Solution().hammingPisoi(73,93))  # 2
print(Solution().hammingPisoi(1,1968))  # 7

