# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

#  Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if not nums:
            return None

        med = len(nums) // 2
        numsleft = nums[:med]
        numsright = nums[med + 1:]

        bst = TreeNode(nums[med])
        bst.left = self.sortedArrayToBST(numsleft)
        bst.right = self.sortedArrayToBST(numsright)

        return bst