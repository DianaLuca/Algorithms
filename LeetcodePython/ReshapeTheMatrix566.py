# You're given a matrix represented by a two-dimensional array,
# and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.
# The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.#
# If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int row
        :type c: int column
        :rtype: List[List[int]]
        """
        n = len(nums)  # lines
        m = len(nums[0])  # columns
        if r * c != n * m:
            return nums

        arr = []
        for i in range(n):
            for j in range(m):
                arr.append(nums[i][j])

        Matrix = [[0 for x in range(c)] for y in range(r)]
        k = 0
        for i in range(r):
            for j in range(c):
                Matrix[i][j] = arr[k]
                k += 1

        return Matrix