# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l)
# there are such that A[i] + B[j] + C[k] + D[l] is zero.
# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
# All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
# Example:
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# Output:
# 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

import bisect


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        h = {}
        for a in A:
            for b in B:
                if a + b in h:
                    h[a + b] += 1
                else:
                    h[a + b] = 1

        res = 0
        for c in C:
            for d in D:
                if -(c + d) in h:
                    res += h[-(c + d)]
        return res


    def fourSumCount_bisect(self, A, B, C, D):
        n = len(A)
        lab = []
        lcd = []

        for i in range(n):
            for j in range(n):
                lab.append(A[i] + B[j])
                lcd.append(C[i] + D[j])

        lcd.sort()

        res = 0
        for el in lab:
            index_left = bisect.bisect_left(lcd, -el, 0, n * n)
            if index_left < n * n and lcd[index_left] == -el:
                index_right = bisect.bisect_right(lcd, -el, 0, n * n)
                d = index_right - index_left
                if (el + lcd[index_left]) == 0:
                    res += d
        return res