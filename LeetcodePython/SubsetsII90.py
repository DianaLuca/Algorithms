# Given a collection of integers that might contain duplicates, nums, return all possible subsets.
#
# Note: The solution set must not contain duplicate subsets.
#
# For example,
# If nums = [1,2,2], a solution is:
#
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]


class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, path + [nums[i]], res)