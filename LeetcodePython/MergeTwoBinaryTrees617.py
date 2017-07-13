# Given two binary trees and imagine that when you put one of them to cover the other,
# some nodes of the two trees are overlapped while the others are not.
#
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
# then sum node values up as the new value of the merged node. Otherwise,
# the NOT null node will be used as the node of new tree.
#
# Example 1:
# Input:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# Output:
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7
# Note: The merging process must start from the root nodes of both trees.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1

        val = (t1.val if t1.val is not None else 0) + (t2.val if t2.val is not None else 0)
        t3 = TreeNode(val)
        t3.left = self.mergeTrees(t1.left, t2.left)
        t3.right = self.mergeTrees(t1.right, t2.right)
        return t3

    res = []

    def print_tree(self, t3, res):
        if t3:
            res.append(t3.val)
        else:
            res.append("None")
        if t3.left:
            self.print_tree(t3.left, res)
        if t3.right:
            self.print_tree(t3.right, res)
        return res

# test case:
# t1 = [1,3,2,5]
# t2 = [2,1,3,null,4,null,7]

t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.right = TreeNode(2)
t1.left.left = TreeNode(5)

t2 = TreeNode(2)
t2.left = TreeNode(1)
t2.right = TreeNode(3)
t2.left.right = TreeNode(4)
t2.right.right = TreeNode(7)

s = Solution()
t3 = s.mergeTrees(t1, t2)
print(s.print_tree(t3, res=[]))

