# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
#
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
# If it does not exist, output -1 for this number.


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        for el in findNums:
            for i, elem in enumerate(nums):
                if el == elem:
                    i += 1
                    while i < n and nums[i] < el:
                        i += 1
                    if i == n:
                        res.append(-1)
                    else:
                        res.append(nums[i])

        return res