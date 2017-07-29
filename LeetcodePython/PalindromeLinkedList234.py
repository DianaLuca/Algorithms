# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        lhrev = None  # lhrev : left half reverse
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            lhrev, lhrev.next, slow = slow, lhrev, slow.next

        if fast:
            slow = slow.next

        while lhrev and lhrev.val == slow.val:
            slow = slow.next
            lhrev = lhrev.next

        return not slow