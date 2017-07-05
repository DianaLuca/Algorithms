# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
# such that nums[i] = nums[j] and the absolute difference between i and j is at most k.


class Solution(object):
    # O(N) time and O(N) space
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}

        for i, el in enumerate(nums):
            if el in d:
                if abs(d[el] - i) <= k:
                    return True
                else:
                    d[el] = i
            else:
                d[el] = i
        return False

    # O(N*logN) time, O(N) space
    def containsNearbyDuplicate_nlogn(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        arr = [(b, a) for a, b in enumerate(nums)]
        arr.sort()
        n = len(nums)

        for i in range(n - 1):
            if arr[i][0] == arr[i + 1][0]:
                if abs(arr[i][1] - arr[i + 1][1]) <= k:
                    return True
        return False