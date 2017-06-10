66# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
# You need to find the shortest such subarray and output its length.
# BruteForce method O(N^2)


def shortestSubarrayN2(A):
    n = len(A)
    if n <= 1:
        return 0

    left = n
    right = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if A[j] < A[i]:
                left = min(left, i)
                right = max(right, j)
    if left > right:
        return 0
    else:
        return right - left + 1


# Sort the list in O(NlogN) and compare it  +O(N) with initial list => O(NlogN) time complexity
def findUnsortedSubarrayNlogN( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n <= 1:
        return 0

    new_list = nums[:]
    nums.sort()
    left = 0
    right = n - 1

    i = 0
    while i < n:
        if nums[i] != new_list[i]:
            break
        while i < n and nums[i] == new_list[i]:
            left += 1
            i += 1

    i = n - 1
    while i > -1:
        if nums[i] != new_list[i]:
            break
        while i > -1 and nums[i] == new_list[i]:
            right -= 1
            i -= 1

    if left > right:
        return 0
    return right - left + 1


# TestCases:
A = []  # 0
print(findUnsortedSubarrayNlogN(A))

B = [2,2,2,2]  # 0
print(findUnsortedSubarrayNlogN(B))

C = [1,2,3,4,5]  # 0
print(findUnsortedSubarrayNlogN(C))

D = [5,4,3,2,1]  # 5
res = findUnsortedSubarrayNlogN(D)
print(res)
assert (res == 5)

E = [1,2,4,3,2,5]  # 3
res = findUnsortedSubarrayNlogN(E)
assert (res == 3)