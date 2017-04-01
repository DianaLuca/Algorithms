# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

from collections import Counter


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = Counter(nums)
        if not d: #dictionary d is empty {}
            return False

        for el in nums:
            if d[el] >= 2:
                return True

        return False