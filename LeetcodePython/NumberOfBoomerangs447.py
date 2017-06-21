# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k)
# such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
# Find the number of boomerangs.
# You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
#
# Example:
# Input:
# [[0,0],[1,0],[2,0]]
#
# Output:
# 2
#
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

from collections import defaultdict


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int 
        """
        result = 0
        for i, p in enumerate(points):
            d = defaultdict(int)
            for j, n in enumerate(points):
                if j != i:
                    d[(n[0] - p[0]) ** 2 + (n[1] - p[1]) ** 2] += 1
            for key, value in d.items():
                result += value * value - value
        return result


    def numberOfBoomerangsSolutionTwo(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(points)):
            d = {}
            for j in range(len(points)):
                if i != j:
                    dist = pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2)
                    count += d.get(dist, 0)
                    d[dist] = d.get(dist, 0) + 1

        return 2*count