# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.


class Solution(object):
    def moveZeroes(self, nums):
        j = 1
        for i in range(len(nums) - 1):
            if nums[i] == 0 and (j < len(nums)):
                while (j < len(nums) - 1) and (nums[j] == 0):
                    j += 1
                nums[i] = nums[j]
                nums[j] = 0
                j += 1
            else:
                j += 1

        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
