import sys
def findMaxAverage( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    n = len(nums)
    if not nums:
        return 0
    sums = [0] * (n - k + 1)
    res = (sum(nums[:k]) * 1.0) / k
    sums[0] = res

    for i in range(1, n - k + 1):
        sums[i] = sums[i - 1] - (nums[i - 1] * 1.0) / k + (nums[i + k - 1] * 1.0) / k
        res = max(res, sums[i])

    return res

# print (findMaxAverage([1,12,-5,-6,50,3], 4))
print (findMaxAverage([1], 1))

def findMaxAverage(nums, k):
    # 0 .. N - 1
    # 0 1 ... N
    # [j, i] -> prefix_sum[i] - prefix_sum[j-1]
    # for i : K ... N:

    N = len(nums)
    nums = [0] + nums

    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i-1] + nums[i]

    sol = -1e18
    for i in range(k, N + 1):
        j = i - k + 1
        sol = max(sol, prefix_sum[i] - prefix_sum[j-1])

    return 1.0 * sol / k