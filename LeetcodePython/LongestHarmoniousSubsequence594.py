# We define a harmonious array is an array where the difference between
# its maximum value and its minimum value is exactly 1.
# Now, given an integer array, you need to find the length of its
# longest harmonious subsequence among all its possible subsequences.

# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# Note: The length of the input array will not exceed 20,000.
# Under ideal circumstances, a high-end desktop x86 processor can execute over 100 billion instructions per second


from collections import Counter


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1: return 0

        res = 0
        d = Counter(nums)
        dkeys = sorted(d.keys())

        for i in range(1, len(dkeys)):
            if dkeys[i] - dkeys[i - 1] == 1:
                res = max(res, d[dkeys[i]] + d[dkeys[i - 1]])
        return res
