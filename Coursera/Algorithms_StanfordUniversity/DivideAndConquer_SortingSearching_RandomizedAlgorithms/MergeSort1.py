# canonical divide and conquer: split in half the array and sort the halves recursively
# and then combine the results into sorted output (this step is called "merge").
# time: O(n*logn)

def mergeSort(lst):
    if len(lst) == 1:
        return lst
    left = mergeSort(lst[0: len(lst)//2])
    right = mergeSort(lst[len(lst)//2: len(lst)])
    # print("left : {}, right: {}".format(left, right))
    return merge(left, right)


def merge(a, b):
    i, j = 0, 0
    n = len(a) + len(b)
    c = [-1] * n
    for k in range(n):
        if i == len(a) or (j < len(b) and a[i] > b[j]):
            c[k] = b[j]
            j += 1
        elif j == len(b) or (i < len(a) and b[j] >= a[i]):
            c[k] = a[i]
            i += 1
        else:
            assert False
    return c

A = [2,1, 4,5]
print("A before mergeSort", A)
print("A after mergeSort", mergeSort(A))

print("merge: ",merge([2, 4, 6], [1, 2, 3]))
