"""
 we can beat this lower bound of O(nlgn) if we can gather information about the sorted order of the input by means other than comparing elements. 
 The counting sort algorithm, for example, assumes that the input numbers are in the set 0,1...k. 
 By using array indexing as a tool for determining relative order, counting sort can sort n numbers in O(k+n) time. 
 Thus, when k = O(n), counting sort runs in time that is linear in the size of the input array.
"""


def counting_sort(A):
    n = len(A)
    valmax = -10e9

    for i in range(n):
        valmax = max(valmax, A[i])

    C = [0] * (valmax+1)
    for i in range(n):
        C[A[i]] += 1
    print(C)

    for i in range(valmax):
        C[i+1] += C[i]
    print(C)


    B = [0] * n
    for i in range(n):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

    return B


def main():
    A = [5, 4, 5, 9, 7, 2]
    assert counting_sort(A) == [2, 4, 5, 5, 7, 9]

if __name__ == '__main__':
    main()
