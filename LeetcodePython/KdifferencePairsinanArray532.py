# Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array.
# Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and
# their absolute difference is k.
#
# Example 1:
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.


from collections import Counter


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > 0:
            a = set(nums)
            b = set(el + k for el in nums)
            # print a & b
            return len(a & b)

        elif k == 0:
            d = Counter(nums)
            # print d
            return sum(v > 1 for v in d.values())

        else:
            return 0
