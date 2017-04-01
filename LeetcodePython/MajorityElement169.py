# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         d = dict()
#         n = len(nums)
#         for el in nums:
#             d[el] = d.get(el, 0) + 1
#
#         for i in range(n):
#             if d[nums[i]] > n//2:
#                 return nums[i]


from collections import Counter


class Solution(object):
    def majorityElement(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """
        d = Counter(nums)

        for el in nums:
            if d[el] > len(nums) // 2:
                return el




