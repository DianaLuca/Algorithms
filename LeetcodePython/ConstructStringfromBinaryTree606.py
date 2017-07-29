"""You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.
The null node needs to be represented by empty parenthesis pair "()". 
And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"
Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        str = []
        stack = [t]
        while stack:
            node = stack.pop()
            if node == "(" or node == ")":
                str.append(node)
            elif node != "()" and node != None:
                str.append(node.val)
                stack.append(")")
                if node.right:
                    stack.append(node.right)
                stack.append("(")
                stack.append(")")
                if node.left:
                    stack.append(node.left)
                elif not node.left and node.right:
                    stack.append("()")
                stack.append("(")
        return str