class Queue(object):
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def isEmpty(self):
        return (len(self.stack1) + len(self.stack2)) == 0

    def size(self):
        return len(self.stack1) + len(self.stack2)

    def push(self, x):
        if self.stack2:
            while len(self.stack2) > 0:
                self.stack1.append(self.stack2.pop())
        self.stack1.append(x)

    def pop(self):
        if self.stack1:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if len(self.stack2) > 0 else "queue is empty"

q = Queue()
print(q.isEmpty())  # True
q.push(1)
q.push(3)
q.push(4)
print("is empty?", q.isEmpty())  # False
print("size =",q.size())
print("pop:", q.pop())  # 1
print("is empty?",q.isEmpty())
print("pop:",q.pop())  # 3
q.push(5)
print("pop:",q.pop())  # 4
print("pop:",q.pop())  # 5
print("pop:",q.pop())  # empty
