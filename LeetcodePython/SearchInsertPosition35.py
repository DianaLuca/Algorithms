# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.
#
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, nr in enumerate(nums):
            n = len(nums)
            if nr == target or nr > target:
                return i
            if i == n-1:
                return n

    def searchInsertBinarySearch(self, nums, target):
        n = len(nums)
        left, right = 0, n

        while left < right:
            mid = (left + right) // 2  # == (left+right)>>1
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left
