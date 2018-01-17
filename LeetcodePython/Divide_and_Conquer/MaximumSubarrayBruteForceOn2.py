"""
Solve the problem using brute force
Complexity O(N^2)
"""
import sys


class Solution(object):
    def maximumSubarrayBruteForce(self, arr):
        n = len(arr)
        res = -sys.maxsize
        left, right = 0,0
        for i in range(n):
            for j in range(i+1, n+1):
                crrsum = sum(arr[i:j])
                if res < crrsum:
                    res = crrsum
                    left = i
                    right = j-1
        return res, left, right

s = Solution()
print(s.maximumSubarrayBruteForce([-1,-2,-10,-3,-1,-4]))
print(s.maximumSubarrayBruteForce([-1,-2,10,3,-1,4]))
