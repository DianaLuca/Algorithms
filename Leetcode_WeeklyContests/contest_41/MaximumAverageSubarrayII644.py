class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        if not nums:
            return 0
        sums = [0] * (n - k + 1)
        res = (sum(nums[:k]) * 1.0) / k
        sums[0] = res

        for i in range(1, n - k + 1):
            sums[i] = sums[i - 1] - (nums[i - 1] * 1.0) / k + (nums[i + k - 1] * 1.0) / k
            res = max(res, max(sums[i], max(sums[i-1], (sums[i-1]*k + nums[i+k-1])*1.0/(i+k))))

        return res