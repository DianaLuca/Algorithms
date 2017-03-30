# Given an array of integers, every element appears twice except for one. Find that single one.

class Solution(object):
    def singleNumber(self, nums):
        unique = 0
        for el in nums:
            unique = unique ^ el
        return unique

print (Solution().singleNumber([1, 3, 2, 3, 1]))