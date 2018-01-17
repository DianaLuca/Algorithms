class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if not self.items:
            return True
        return False

    def peek(self):
        return self.items[len(self.items)-1]

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

