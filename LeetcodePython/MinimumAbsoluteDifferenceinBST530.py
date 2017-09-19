"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

Note: There are at least two nodes in this BST.
"""
import sys


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorder(self, root, res):
        if not root:
            return res
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)
        return res

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.inorder(root, res)

        for i in range(len(res)):
            if i == 0:
                dif = sys.maxsize
            else:
                dif = min(dif, res[i] - res[i - 1])
        return dif

