import random, time

size1 = 100
A = [random.randint(0, 10) for _ in range(size1)]
print(A)
t2 = time.clock()
#countingSort(A)
print("Counting Sort(size =", str(size1),"):", (time.clock()-t2) * 1000)
print(A)
