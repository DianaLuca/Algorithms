# Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.


class Solution(object):
    # Rotate to the Right
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    # Rotate to the Left
    def leftRotate(self, nums, k):
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, n-k, n-1)
        self.reverse(nums, 0, n-k-1)

    def reverse(self, A, x, y):
        while x < y:
            tmp = A[x]
            A[x] = A[y]
            A[y] = tmp
            x += 1
            y -= 1


s = Solution()
A = [1,2,3,4,5,6,7]
print(A)
s.leftRotate(A,3)
print(A)
