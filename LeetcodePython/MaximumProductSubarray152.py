# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = nums[0]
        max_prod = res
        min_prod = res

        for i in range(1, n):
            # if it's a negative value, max becomes min, min becomes max
            if nums[i] < 0:
                tmp = max_prod
                max_prod = min_prod
                min_prod = tmp

            max_prod = max(nums[i], max_prod * nums[i])
            min_prod = min(nums[i], min_prod * nums[i])

            res = max(res, max_prod)

        return res
