"""
The overall time is O(k+n). In practice, we usually use counting sort when we have k = n, in which case the running time is O(n)
"""
import random, time


def countingSort(A):
    n = len(A)
    minel = min(A)
    maxel = max(A)
    nrC = maxel-minel + 1

    cnt = [0] * nrC
    for el in A:
        cnt[el-minel] += 1

    k = 0
    for i, el in enumerate(cnt):
        for j in range(el):
            A[k] = i
            k += 1
    return A


size1 = 100
A = [random.randint(0, 10) for _ in range(size1)]
print(A)
t2 = time.clock()
countingSort(A)
print("Counting Sort(size =", str(size1),"):", (time.clock()-t2) * 1000)
print(A)
