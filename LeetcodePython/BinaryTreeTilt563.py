# Given a binary tree, return the tilt of the whole tree.
# The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values
# and the sum of all right subtree node values. Null node has tilt 0.
# The tilt of the whole tree is defined as the sum of all nodes' tilt.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    res = 0

    def calculate_tilt(self, root):
        if not root:
            return 0
        left = self.calculate_tilt(root.left)
        right = self.calculate_tilt(root.right)
        self.res += abs(left - right)
        return left + right + root.val

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.calculate_tilt(root)
        return self.res

