# “Given an array A and a target value,
# return the index of the first element in A equal to or greater than the target value.”
# Source: TCO topcoder.com

def searchLowerBound(A, target):
    n = len(A)
    l, r = 0, n
    while l < r:
        m = l + (r - l)//2
        # Consider the predicate “Is A[x] greater than or equal to the target value?”
        # Keep your eye out for overflow errors all around, especially in calculating the median.
        if A[m] >= target:
            r = m
        else:
            l = m + 1
    return l if A[l] == target else -1


print(searchLowerBound([1,2], 2))


def searchUpperBound(A, target):
    n = len(A)
    l, r = 0, n
    while l < r:
        m = l + (r - l + 1)//2
        # Consider the predicate “Is A[x] greater than or equal to the target value?”
        # Keep your eye out for overflow errors all around, especially in calculating the median.
        if A[m] >= target:
            r = m
        else:
            l = m + 1
    return l if A[l] == target else -1


print(searchUpperBound([1,3], 3))
