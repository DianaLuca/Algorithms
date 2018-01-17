"""
Insertion Sort
O(N^2) time complexity (two interwound whiles)

Insertion sort, merge sort, heapsort, and quicksort are all comparison sorts:
They determine the sorted order of an input array by comparing elements.
We prove a lower bound of nlgn on the worst-case running time of any comparison sort on n inputs, 
thus showing that heapsort and merge sort are asymptotically optimal comparison sorts
"""


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def insertionSort(arr):
    n = len(arr)
    i = 1
    while i < n:
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            swap(arr, j-1, j)
            j -= 1
        i += 1
    return arr

arr = [7,1,2,3]
insertionSort(arr)
print(arr)
