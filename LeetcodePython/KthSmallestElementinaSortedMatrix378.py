# Given a n x n matrix where each of the rows and columns are sorted in ascending order,
# find the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
# Example:
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
# return 13.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n2.


class Solution(object):

    # time complexity: O(N + NlogN) = O(NlogN)
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        arr = []
        for marr in matrix:
            arr += marr
        arr.sort()
        return arr[k-1]


    # O(N)
    def kthSmallest_binarySearch(self, matrix, k):
        if not matrix:
            return 0

        n = len(matrix)
        lo = matrix[0][0]
        hi = matrix[-1][-1]  # last element matrix[n-1][n-1]
        while lo < hi:
            mid = (lo+hi) >> 1
            j = n-1
            count = 0
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += j+1
            if count < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

