"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        t = ListNode(0)
        r = t
        rem = 0

        while l1 and l2:
            v = l1.val + l2.val + rem
            t.val = v % 10
            rem = (v - t.val) / 10
            if l1.next or l2.next or rem:
                t.next = ListNode(0)
                t = t.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            v = l1.val + rem
            t.val = v % 10
            rem = (v - t.val) / 10
            if l1.next or rem:
                t.next = ListNode(0)
                t = t.next
            l1 = l1.next

        while l2:
            v = l2.val + rem
            t.val = v % 10
            rem = (v - t.val) / 10
            if l2.next or rem:
                t.next = ListNode(0)
                t = t.next
            l2 = l2.next
        if rem:
            t.val = rem

        return r
