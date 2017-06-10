def insertionSort(A):
    n = len(A)
    cnt = 0
    for i in range(1, n):
        j = i
        while j > 0 and A[j-1] > A[j]:
            swap(A, j-1, j)
            j -= 1
            cnt += 1
    return cnt


def NOTinsertionS(A):
    n = len(A)
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            cnt += 1
            if A[i] > A[j]:
                swap(A, i, j)
    return cnt


def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp


def quadraticTime(n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += 1
    return cnt

A = [5,4,3,2,1,4,4,5,5]
Aa = [1,2,3,4,5]
print('Before InsertionSort, A = ', A)
stepnotis = NOTinsertionS(A)  # O(N^2) best case
print('After NOTinsertionSort, A = {} in {} steps'.format(A, stepnotis))

print('-------- The real IS --------')
print("before IS:",Aa)
stepis = insertionSort(Aa)  # best case O(N)
print('After InsertionSort: {} in {} steps'.format(Aa, stepis))

print('quadraticTime({}) in : {} time'.format(3, quadraticTime(3)))