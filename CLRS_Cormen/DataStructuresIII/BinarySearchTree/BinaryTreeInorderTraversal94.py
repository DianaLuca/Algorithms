"""
Given a Binary Search Tree return the inorder traversal of it's nodes' values with an iterative solution

example:
given [1, null, 2, 3]
return [1, 3, 2]
"""


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rec(val, N):
    if val > N:
        return None
    return Node (val, left=rec(2*val, N), right=rec(2*val+1, N))


def make_big_tree(N):
    return rec(1, N)


class Solution(object):
    def pisoi(self, root):
        st = [root]
        ret = []

        while st:
            el = st[-1]
            st.pop()
            if type(el) == int:
                ret.append(el)
            elif el:
                if el.right:
                    st.append(el.right)
                st.append(el.val)
                if el.left:
                    st.append(el.left)
        return ret

    def inorderTraversal(self, root):
        stk, res = [], []
        op = 0
        while root:
            stk.append(root)
            root = root.left
            op += 1
        while stk:
            node = stk.pop()
            res.append(node.val)
            op += 1
            if node.right:
                right = node.right
                op += 1
                while right:
                    stk.append(right)
                    right = right.left
                    op += 1
        print (op)
        return None

#tree = Node(1, Node(7, Node(10, None, None), Node(2, None, None)), Node(8, Node(3, None, None), None))
#tree = Node(1, right=Node(2, right=Node(3, left=Node(4))))
big_tree = make_big_tree(100000)
s = Solution()

print(s.inorderTraversal(big_tree))
