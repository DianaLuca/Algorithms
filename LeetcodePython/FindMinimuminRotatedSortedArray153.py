# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Find the minimum element.
# You may assume no duplicate exists in the array.


class Solution():
    # BinarySearch O(logN)
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n-1

        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left] if nums[left] <= nums[right] else nums[right]

    # Linear O(N)
    def findMin_linear(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)