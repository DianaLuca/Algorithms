# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if (target >= nums[left]) and (target < nums[mid]):
                    right = mid - 1
                else:  # (target <= nums[left]) or (target > nums[mid])
                    left = mid + 1

            else:  # nums[left] > nums[mid]
                if (target > nums[mid]) and (target <= nums[right]):
                    left = mid + 1
                else:  # (target < nums[mid]) or (target >= nums[right])
                    right = mid - 1

        return left if nums[left] == target else -1