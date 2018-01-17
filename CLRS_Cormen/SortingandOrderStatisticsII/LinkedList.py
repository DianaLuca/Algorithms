class Node(object):
    def __init__(self, x):
        self.next = None
        self.val = x


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)

        else:
            n = self.head

            while n.next:
                n = n.next
            n.next = Node(data)
        return

    def length(self):
        if not self.head:
            return 0
        length = 1
        n = self.head
        while n.next:
            length += 1
            n = n.next
        return length

    def isEmpty(self):
        return not self.head

    def printList(self):
        n = self.head
        if not self.head:
            print("")
        else:
            while n:
                print(n.val, end=", ")
                n = n.next


ll = LinkedList()
elem = [1,2,3,4,5]
for el in elem:
    ll.append(el)
ll.printList()
print("is empty? ",ll.isEmpty())
print("what is linked list's length? ",ll.length())