class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isSymmetricTwo(root, root)

    def isSymmetricTwo(self, t1 = TreeNode, t2 = TreeNode):
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        return t1.val == t2.val and self.isSymmetricTwo(t1.right, t2.left) and self.isSymmetricTwo(t1.left, t2.right)