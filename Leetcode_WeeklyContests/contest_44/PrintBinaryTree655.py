"""
Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
Each unused space should contain an empty string "".
Print the subtrees following the same rules.

Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getTreeHight(self, root):
        if not root:
            return 0
        return 1 + max(self.getTreeHight(root.left), self.getTreeHight(root.right))

    def printMyTree(self, res, root, m, n, h, w):
        if not root:
            return
        level = m
        pos = (n + w)//2
        res[level][pos] = str(root.val)
        self.printMyTree(res, root.left, level + 1, n, h, pos)
        self.printMyTree(res, root.right, level + 1, pos + 1, h, w)

    def printTree(self, root):
        """
        :param root: TreeNode 
        :return: List[List[str]]
        """
        res = list()
        height = self.getTreeHight(root)  # nr of lines
        wide = pow(2, height) - 1  # nr of columns
        for i in range(height):
            tmpcol = list()
            for j in range(wide):
                tmpcol.append("")
            res.append(tmpcol)
        self.printMyTree(res, root, 0, 0, height - 1, wide - 1)
        return res

