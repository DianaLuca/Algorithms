"""Given an m * n matrix M initialized with all 0's and several update operations.
Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, 
which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.
You need to count and return the number of maximum integers in the matrix after performing all the operations.

Input: 
m = 3, n = 3
operations = [[2,2],[3,3]]
Output: 4

Note:
The range of m and n is [1,40000].
The range of a is [1,m], and the range of b is [1,n].
The range of operations size won't exceed 10,000.
"""
import sys


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n

        min_ln, min_col = sys.maxsize, sys.maxsize
        for op in ops:
            min_ln = min(min_ln, op[0])
            min_col = min(min_col, op[1])

        return min_ln * min_col
