from heapq import heapify, heappop, heappush

"""
see: https://docs.python.org/3.0/library/heapq.html
Heaps are arrays for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k, counting elements from zero.
"""

lst = [7,3,2,5,7,4,1]
print("lst before heapify:", lst)
heapify(lst)
print("lst after heapify:", lst)


heap = []
data = [1,3,5,7,9,2,4,6,8]
for el in data:
    heappush(heap, el)
print(heap)
ordered = []
while heap:
    ordered.append(heappop(heap))
print(ordered)



