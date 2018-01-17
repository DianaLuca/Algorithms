"""
Input: root node, key
output: predecessor node, successor node

1. If root is NULL
      then return
2. if key is found then
    a. If its left subtree is not null
        Then predecessor will be the right most 
        child of left subtree or left child itself.
    b. If its right subtree is not null
        The successor will be the left most child 
        of right subtree or right child itself.
    return
3. If key is smaller then root node
        set the successor as root
        search recursively into left subtree
    else
        set the predecessor as root
        search recursively into right subtree
"""


class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def maxBST(root):
    if not root.right:
        return root
    return maxBST(root.right)

def minBST(root):
    if not root.left:
        return root
    return minBST(root.left)


def findPredSucc(root, key):
    if not root:
        return

    if root.key == key:
        if root.left:
            findPredSucc.predecessor = maxBST(root.left)  # the predecessor is the right most child of left subtree
        if root.right:
            findPredSucc.successor = minBST(root.right)
        return

    # If key is smaller than root's key, go to left subtree
    if root.key > key:
        findPredSucc.successor = root
        findPredSucc(root.left, key)

    else:  # go to right subtree
        findPredSucc.predecessor = root
        findPredSucc(root.right, key)


bst = Node(20)
bst.left = Node(10)
bst.left.left = Node(5)
bst.left.right = Node(15)
bst.right = Node(22)

findPredSucc.predecessor = Node(None)
findPredSucc.successor = Node(None)

findPredSucc(bst,bst.key)
print(findPredSucc.successor.key, findPredSucc.predecessor.key)
