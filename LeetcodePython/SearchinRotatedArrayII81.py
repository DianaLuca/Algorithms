# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
# Would this affect the run-time complexity? How and why?
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Write a function to determine if a given target is in the array.
# The array may contain duplicates.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:  # 0 <= 1
            mid = left + ((right - left) >> 1)

            if nums[mid] == target:
                return True

            if nums[mid] == nums[left]:
                while left <= right and nums[mid] == nums[left]:
                    left = left + 1
            elif nums[left] < nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:  # nums[left] > nums[mid]
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return False
