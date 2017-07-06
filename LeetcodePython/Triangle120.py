# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space,
# where n is the total number of rows in the triangle.


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if n == 1:
            return triangle[0][0]

        old = triangle[-1][:]

        for i in reversed(range(n - 1)):
            new = triangle[i]
            for j in range(i+1):
                new[j] += min(old[j], old[j + 1])
            old = new[:]

        return new[0]
