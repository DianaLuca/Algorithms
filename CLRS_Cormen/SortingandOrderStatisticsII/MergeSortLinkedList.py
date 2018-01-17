"""
Sort a linked list by using merge sort algorithm
1. recursively do merge sort on each halves. Base Case: linked list have one element. return it
2. split the given linked list into halves
3. merge in ascending order the 2 sub-linked-lists

Not finished yet! just scratched some ideas
"""

from .LinkedList import LinkedList, Node


def mergeLL(A, B):
    n = A.length()
    m = B.length()
    res = Node()
    if n == 0:
        return B
    if m == 0:
        return A
    if A.val <= B.val:
        res.val = A.val
        res.next = mergeLL(A.next, B)
    else:
        res.val = B.val
        res.next = mergeLL(A, B.next)
    return res


def splitLinkedList(list):
    left = LinkedList()
    right = LinkedList()
    size = list.length()
    for i in range(size//2):
        left.val = list.head.val
        list = list.next
        left.next = Node()
    right = list
    return left, right


def mergeLinkedList(list):
    n = list.length()
    if n <= 1:
        return list
    left, right = splitLinkedList(list)
    mergeLinkedList(left)
    mergeLinkedList(right)
    return mergeLL(left, right)

