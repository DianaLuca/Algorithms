"""
Complexity: O(n*logn)
T(n) = 2*T(n/2) + n
n - is the size of problem
2 - (a - from Master Theorem) is the number of subproblems in recursion
n/2 - (n/b - from Master Theorem) is the size of each problem in recursion
+n - (f(n) - from Master Theorem) is the cost of the work done outside the recursive calls (niddle sum calculus)
"""


def max_sum_subarray(arr, left, right):
    center = (left + right)//2
    if left == right:
        if arr[left] > 0:
            return arr[left]
        else:
            return 0

    maxLeftSum = max_sum_subarray(arr, left, center)
    maxRightSum = max_sum_subarray(arr, center+1, right)

    leftSum = 0
    rightSum = 0
    crrsum = 0
    for i in range(center, left-1, -1):
        crrsum += arr[i]
        if crrsum > leftSum:
            leftSum = crrsum
    crrsum = 0
    for i in range(center+1, right+1):
        crrsum += arr[i]
        if crrsum > rightSum:
            rightSum = crrsum

    return max(leftSum + rightSum, maxRightSum, maxLeftSum)


arr = [-9, -9, -10, -11, -4, -1, -2]
print(max_sum_subarray(arr, 0, len(arr)-1))