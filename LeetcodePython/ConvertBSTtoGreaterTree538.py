""" Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST
# is changed to the original key plus sum of all keys greater than the original key in BST.
# Example:
#
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
#
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    keepsum = 0

    def right_sum_convertBST(self, root):
        if not root:
            return
        self.right_sum_convertBST(root.right)
        root.val = root.val + self.keepsum
        self.keepsum = root.val
        self.right_sum_convertBST(root.left)

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.right_sum_convertBST(root)
        return root