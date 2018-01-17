"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""


from collections import Counter


class Solution(object):

    def findShortestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cd = Counter(nums)

        res = n
        maxd = max(cd.values())

        first, last = {}, {}
        for i, el in enumerate(nums):
            if el not in first:
                first[el] = i

        nums.reverse()
        for i, el in enumerate(nums):
            if el not in last:
                last[el] = n-1-i

        nums.reverse()

        for key, value in cd.items():
            if value == maxd:
                res = min(res, last[key] - first[key] + 1)
        return res

