"""
Given a sorted array, two integers k and x, find the k closest elements to x in the array. 
The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]

Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 10^4
Absolute value of elements in the array and x will not exceed 10^4
"""


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :param arr: array
        :param k: int
        :param x: int
        :return: array
        """
        res = []
        for el in arr:
            if k > len(res):
                res.append(el)
            elif abs(el - x) < abs(res[0] - x):
                res = res[1:]
                res.append(el)
        return res

