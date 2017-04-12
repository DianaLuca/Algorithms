# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]



class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # res = [[] for x in xrange(numRows)]

        res = []

        for i in range(numRows):
            res.append([1] * (i + 1))

            if i > 1:
                for j in range(1, i):
                    res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res