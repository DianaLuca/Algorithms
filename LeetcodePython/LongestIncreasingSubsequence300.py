# Given an unsorted array find the longest increasing subsequence.
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
# Note that there may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.


class Solution():
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [0] * n
        res = -1

        for i in range(n):
            dp[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    res = max(res, dp[i])
        return res

# test case
s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))  # 4
