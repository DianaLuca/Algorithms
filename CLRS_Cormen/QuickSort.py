def quickSort(A, p, r):
    print('A = ',A)
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)


def partition(A, p, r):
    x = A[r]  # last element from A
    i = p-1
    for j in range(p, r):
        if A[j] <= x:  # A[j]=4, x=1
            i += 1  # i = 0, i = 1
            swap(A, i, j)
            print(A, 'in for, if')

    swap(A, i+1, r)
    print(A, 'before return')
    k = i+1
    print('return i =',k)
    return i+1


def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp


A = [1,2,3,4]
print(A)
quickSort(A,0,len(A)-1)
print(A)