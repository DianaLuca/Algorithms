# how many inversions does this array have?
# we need to look for pairs of array entries so that the earlier or left entry is bigger than the later or right entry.
# Brute Force Method: O(n^2)

def calculateInversions(a):
    res = 0

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                res += 1

    return res

A = [2,4,6,1,3,5]
print(calculateInversions(A))