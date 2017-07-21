"""Given a binary tree, return the preorder traversal of its nodes' values.
For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # Iterative Solution
    def preorderTraversal_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Preorder (Root, Left, Right)
        lst = []
        lst_stack = [root]
        while lst_stack:
            node = lst_stack.pop()
            if node:
                lst.append(node.val)
                lst_stack.append(node.right)
                lst_stack.append(node.left)
        return lst

    # Recursive:
    def preorder(self, root, lst):
        if not root:
            return
        lst.append(root.val)
        self.preorder(root.left, lst)
        self.preorder(root.right, lst)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Preorder (Root, Left, Right)
        lst = []
        self.preorder(root, lst)
        return lst
