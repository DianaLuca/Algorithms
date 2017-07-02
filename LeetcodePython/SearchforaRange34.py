# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

import bisect

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = bisect.bisect_left(nums, target, 0, len(nums))
        right = bisect.bisect_right(nums, target, 0, len(nums))

        if left == right:
            return [-1, -1]
        else:
            return [left, right - 1]