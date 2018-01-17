"""
O(N^2) worst and average time complexity
inplace memory
good for short sequences almost sorted already
not good for long sequences
O(N) time for arrays already sorted
"""
import random
import time


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def bubble_sort(arr):
    n = len(arr)
    cond = True

    while cond:
        cond = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                swap(arr, i-1, i)
                cond = True
        if cond:
            n -= 1
    return arr


def main():
    size1 = 10000
    arr = [random.randint(0, 100000) for _ in range(size1)]
    t2 = time.clock()
    bubble_sort(arr)
    print("Bubble Sort(size=", str(size1), "): ", (time.clock() - t2) * 1000)


if __name__ == '__main__':
    main()
