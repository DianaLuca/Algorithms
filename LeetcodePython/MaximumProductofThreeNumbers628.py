# Given an integer array, find three numbers whose product is maximum and output the maximum product.
# Example 1:
# Input: [1,2,3]
# Output: 6

# Note:
# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        return max(nums[0]*nums[1]*nums[n-1], nums[n-3]*nums[n-2]*nums[n-1])
