# Given an array of integers, every element appears twice except for one. Find that single one.

class Solution(object):
    def singleNumber(self, nums):
        unique = nums[0]
        for i in range(1, len(nums)):
            unique = unique ^ nums[i]

        return unique