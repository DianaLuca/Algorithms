# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


class Solution(object):

    # O(N) space and time complexity (only one list traverse,
    # each look up in the dictionary costs O(1))
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        ndict = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in ndict.values():
                return [i, ndict.keys()[ndict.values().index(dif)]]
            ndict[i] = nums[i]

        return []


    def twoSumDictv2(self, nums, target):
        """
         :type nums: List[int]
         :type target: int
         :rtype: List[int]
        """
        hasht = {k: v for v, k in enumerate(nums)}
        for i, el in enumerate(nums):
            res = target - el
            if hasht.get(res) != None and hasht.get(res) != i:
                return [i, hasht[res]]
        return []


    # O(N^2) time complexity
    # O(1) space complexity
    def twoSumBruteF(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            dif = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == dif:
                    return [i, j]
                j += 1

        return []
