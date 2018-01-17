class Heap(object):

    def __init__(self):
        self.heap = []
        self.N = 0

    def push(self, item):
        self.heap.append(item)



    def pop(self):
        pass

    def siftup(self):
        pass

    def siftdown(self):
        pass

    def heapify(self, x):
        """ Transform list x into a heap in place in O(N) time """
        n = len(x)
        self.siftup()


    # left = None
    # right = None
    #
    # def maxHeapify(self, A, i):
    #     l = self.left(i)
    #     r = self.right(i)
    #     if l <= A.heap_size and A[l] > A[i]:
    #         largest = l
    #     else:
    #         largest = i
    #     if r < A.heap_size and A[r] > A[largest]:
    #         largest = r
    #
    #     if largest != i:
    #         tmp = A[i]
    #         A[i] = A[largest]
    #         A[largest] = tmp
    #         self.maxHeapify(A, largest)
    #
    # def buildMaxHeap(self, A):
    #     A.heap_size = A.length()
    #     for i in range(A.length()//2, 1, -1):
    #         self.maxHeapify(A, i)
    #
