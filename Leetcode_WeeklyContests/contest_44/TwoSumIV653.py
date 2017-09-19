"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # Traverse BST inorder, use O(N) memory to save all values in list lst
    def inorder(self, root, lst):
        if not root:
            return
        self.inorder(root.left, lst)
        lst.append(root.val)
        self.inorder(root.right, lst)
        return lst

    # O(N) time, O(N) memory
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        lst = list()
        lst = self.inorder(root, lst)
        start = 0
        end = len(lst) - 1
        while start < end:
            if lst[start] + lst[end] == k:
                return True
            elif lst[start] + lst[end] > k:
                end -= 1
            else:
                start += 1
        return False

    # -------- other solution

    def findTargetStack(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        vals = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val in vals:
                    return True
                vals.add(k - node.val)
                stack.append(node.left)
                stack.append(node.right)
        return False