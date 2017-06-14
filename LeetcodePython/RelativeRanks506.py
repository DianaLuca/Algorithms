from copy import copy


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        d = {}
        for i, score in enumerate(nums):
            d[score] = i

        nums.sort()
        nums.reverse()
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        res = copy(nums)

        for i, score in enumerate(nums):
            rank = i + 1
            if rank <= 3:
                res[d[score]] = medals[rank - 1]
            else:
                res[d[score]] = str(rank)

        return res
