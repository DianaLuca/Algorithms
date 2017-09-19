"""
Breadth-First Search ( or Traversal) also know as Level Order Traversal.
What is Breadth First Search:

Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. 
It starts at the tree root and explores the neighbor nodes first, before moving to the next level neighbors. 
Approach:

Take a Empty Queue.
Start from the root, insert the root into the Queue.
Now while Queue is not empty,
Extract the node from the Queue and insert all its children into the Queue.
Print the extracted node.
"""

import queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def traverse(self, root):
        print("---------- traverse(): -----------")
        thislevel = [root]
        while thislevel:
            nextlevel = list()
            for r in thislevel:
                print(r.val, end=" ")
                if r.left:
                    nextlevel.append(r.left)
                if r.right:
                    nextlevel.append(r.right)
            print()
            thislevel = nextlevel

    def levelOrderQueue(self, root):
        print("----------- levelOrderQueue(): -----------")
        q = queue.Queue()
        s = set()
        if not root:
            return
        s.add(root)
        q.put(root)
        while not q.empty():
            curr = q.get()
             # if curr is the goal:
             #      return curr
            print(curr.val)
            if curr.left is not None and curr.left not in s:
                s.add(curr.left)
                q.put(curr.left)
            if curr.right is not None and curr.right not in s:
                s.add(curr.right)
                q.put(curr.right)


bt = TreeNode(12)
bt.left = TreeNode(3)
bt.left.left = TreeNode(1)
bt.left.right = TreeNode(7)
bt.right = TreeNode(40)
bt.right.left = TreeNode(30)
bt.right.right = TreeNode(50)
s = Solution()
s.levelOrderQueue(bt)
s.traverse(bt)