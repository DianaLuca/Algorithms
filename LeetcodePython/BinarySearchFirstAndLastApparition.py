# Given an array A of n elements with values A0 ... An−1, sorted such that A0 ≤ ... ≤ An−1,
# and target value T, the following subroutine finds the left boundary index of elements equal T in A.
# Source: Wikipedia


def firstApparition(nums, target):
    n = len(nums)
    l, r = -1, n-1
    while r - l > 1:
        print("left {} right {}".format(l, r))
        m = (l + (r - l)) >> 1
        if nums[m] < target:
            l = m
        else:
            r = m
    if nums[r] == target:
        return r
    return r if nums[r] == target else -1


tests = [(([2, 2, 2, 2, 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2], 2), 0),
         (([1, 1, 1, 2, 2, 2, 2, 2], 2), 3),
         (([1, 1, 1, 2, 2, 2, 2, 2], 3), -1)]

for test in tests:
    input, output = test
    my_output = firstApparition(input[0], input[1])
    if output != my_output:
        print("Error for {}: {} ! {}".format(test, my_output, output))


# And the following subroutine finds the right boundary index of T in A.

def lastApparition(nums, el):
    n = len(nums)
    l, r = 0, n
    while r - l > 1:
        m = (l + (r-l)) >> 1
        if nums[m] <= el:
            l = m
        else:  # nums[m] > el
            r = m
    return l if nums[l] == el else -1

tests = [(([2, 2, 2, 2, 2,2,2,2,2,2,2], 2), 10),
        (([], 1), -1),
         (([1, 1, 1, 2, 2, 2, 2, 2], 2), 7),
         (([1, 1, 1, 2, 2, 2, 2, 2], 3), -1)]

# for test in tests:
#     input, output = test
#     my_output = lastApparition(input[0], input[1])
#     if output != my_output:
#         print("Error for {}: {} ! {}".format(test, my_output, output))
