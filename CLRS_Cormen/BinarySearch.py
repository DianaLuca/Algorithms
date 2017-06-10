def binsrch(a, x):
    if len(a) == 0:
        return -1
    return bs(a,x,0,len(a)-1)


def bs(a,x,i,j):
    if i > j:
        return -1
    m = (i+j) // 2
    if A[m] == x:
        return m
    elif A[m] < x:
        return bs(a, x, m+1, j)
    else:
        return bs(a, x, i, m-1)


A = [1,3,7,13,98]
x = 13
i = binsrch(A, x)
print(i)