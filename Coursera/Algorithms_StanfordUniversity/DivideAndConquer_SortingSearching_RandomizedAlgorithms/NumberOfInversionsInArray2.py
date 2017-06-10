# Count the number of inversions and sort piggybacking on MergeSort
# time: O(n * logn)

def Sort_and_Count(a, n):
    if n == 1:
        return 0
    else:
        x = Sort_and_Count(a[0:n//2], n//2)
        y = Sort_and_Count(a[n//2: n], n-n//2)
        z = Merge_and_Count_Split_Inversions(a, n)

    return x+y+z

def Merge_and_Count_Split_Inversions(a, n):
    l = a[0 :n//2]
    r = a[n//2 : n]
    i, j = 0, 0
    c = [-1] * n
    count = 0
    for k in range(n):
        if i == n//2 or ( j < n-n//2 and l[i] > r[j] ):
            c[k] = r[j]
            j += 1
            count += n//2 - i
        elif j == n-n//2 or ( i < n//2 and r[j] >= l[i] ):
            c[k] = l[i]
            i += 1
        else:
            assert False
    print(c)
    return count

# A = (1,3,5,2,4,6)
A = [2,4,6,1,3,5]
print(Sort_and_Count(A, len(A)))
print('A after merge-and-count-and-sort...', A)