# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
# Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.



class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def deleteNode(self, node):
        tmp = node.next
        node.val = tmp.val
        node.next = tmp.next


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)

S = Solution()
S.deleteNode(node.next.next)

while node:
    print (node.val)
    node = node.next