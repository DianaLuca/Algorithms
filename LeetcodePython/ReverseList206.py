# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            nextTemp = current.next
            current.next = prev
            prev = current
            current = nextTemp
        return prev

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    # def reverseList(self, head):
    #     if head is None or head.next is None:
    #         return head
    #
    #     p = self.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return p
        """
        :type head: ListNode
        :rtype: ListNode
        """

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.val)
            temp = temp.next



list = Solution()
list.push(1)
# list.printList()
list.push(2)
# list.printList()
list.push(3)
list.printList()


list.reverseList(list.head)
list.printList()

