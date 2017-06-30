def countingSortPositives(nums):

    if not nums: return []

    M = max(nums)

    count = [0] * (M+1)

    for el in nums:
        count[el] += 1

    j = 0
    for i, el in enumerate(count):
        for k in range(el):
            nums[j] = i
            j += 1
    return nums

print(countingSortPositives([]))
print(countingSortPositives([1,0]))
print(countingSortPositives([1,0,2,3,9,2,1,14,13,12,1]))


def countingSortNegatives(nums):

    if not nums: return []

    m = min(nums)
    M = max(nums)

    count = [0]*(M-m+1)

    # nums = [3,4,-2]
    # count = [0]*[4 - -2 + 1] = [0,0,0,0,0,0,0] -> [0]*7
    for el in nums:
        count[el-m] += 1    # count[5] = 1, count[6] = 1, count[0] = 1
                            # count = [1,0,0,0,0,1,1]

    j = 0
    for i, c in enumerate(count):
        for k in range(c):
            nums[j] = i + m
            j += 1
    return nums

print(countingSortNegatives([]))
print(countingSortNegatives([1,0,-3]))
print(countingSortNegatives([1,0,2,3,9,-7,-1,5,-3]))