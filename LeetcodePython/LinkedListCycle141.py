# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # initHead = head

        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow.val != fast.val:
            if not slow.next or not fast.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True