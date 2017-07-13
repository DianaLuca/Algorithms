""" Find the kth smallest element in an unsorted array of non-negative integers.
#
# https://www.interviewbit.com/problems/kth-smallest-element-in-the-array/
#
# Definition of kth smallest element
#
# kth smallest element is the minimum possible n such that there are at least k elements in the array <= n.
# In other words, if the array A was sorted, then A[k - 1] ( k is 1 based, while the arrays are 0 based )
# NOTE
# You are not allowed to modify the array ( The array is read only ).
# Try to do it using constant extra space.
#
# Example:
#
# A : [2 1 4 3 2]
# k : 3
# answer : 2
"""


class Solution:
    """ @param A : tuple / array of integers
    # @param B : integer
    # @return an integer
    """
    def kthsmallest(self, A, k):
        minel = min(A)
        maxel = max(A)

        while minel <= maxel:
            elem = (minel + maxel) >> 1
            cnt = self.nr_of_elements(A, elem)

            if cnt == k:
                return self.find_element(A, elem)
            elif cnt < k:  # elem is too small
                minel = elem + 1
            else:  # cnt > k: elem is too big
                maxel = elem - 1
        return minel

    def nr_of_elements(self, A, elem):
        cnt = 0
        for el in A:
            if el <= elem:
                cnt += 1
        return cnt

    def find_element(self, A, elem):
        firstel = -sys.maxsize
        for el in A:
            if el == elem:
                return elem
            if el < elem:
                firstel = max(firstel, el)
        return firstel

