from collections import Counter


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    subtrees = []
    leafs = []

    def isEqual(self, s, t):
        if not (s and t):
            return t is s
        else:
            return (s.val == t.val) and self.isEqual(s.left, t.left) and self.isEqual(s.right, t.right)

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        if not root:
            return []

        if not root.left and not root.right:
            self.leafs.append(root.val)
            return

        if root.left and root.right and self.isEqual(root.left, root.right):
            self.subtrees.append(root.left)

        self.findDuplicateSubtrees(root.left)
        self.findDuplicateSubtrees(root.right)

        dlf = Counter(self.leafs)
        for leaf in dlf.keys():
            if dlf[leaf] > 1:
                self.subtrees.append([leaf])
        return self.subtrees
