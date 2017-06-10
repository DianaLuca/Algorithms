def countingSort(A):
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

    A = B
    print(A)

A = [5,4,5,9,7,2]
countingSort(A)