# Given a binary array, find the maximum number of consecutive 1s in this array.
# Input: [1,1,0,1,1,1]
# Output: 3


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        maxones, nrone = 0, 0
        while i < n:
            if nums[i] == 0:
                maxones = max(maxones, nrone)
                nrone = 0
                i += 1
            while i < n and nums[i] == 1:
                nrone += 1
                i += 1
        maxones = max(maxones, nrone)
        return maxones

#test
print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))