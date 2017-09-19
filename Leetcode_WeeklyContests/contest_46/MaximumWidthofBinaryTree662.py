"""
Given a binary tree, write a function to get the maximum width of the given tree. 
The width of a tree is the maximum width among all levels. 
The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:
Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = [0]
        left = {}

        def dfs(n, pos, level):
            if not n:
                return
            if level not in left:
                left[level] = pos
            else:
                left[level] = min(left[level], pos)
            ret[0] = max(ret[0], pos - left[level])
            dfs(n.left, pos * 2 - 1, level + 1)
            dfs(n.right, pos * 2, level + 1)

        dfs(root, 1, 0)
        return ret[0] + 1


bt = TreeNode(12)
bt.left = TreeNode(3)
bt.left.left = TreeNode(1)
bt.left.right = TreeNode(7)
bt.right = TreeNode(40)
bt.right.left = TreeNode(30)
bt.right.right = TreeNode(50)
bt.left.left.left = TreeNode(1)
bt.right.right.left = TreeNode(55)
s = Solution()
print(s.widthOfBinaryTree(bt))