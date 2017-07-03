"""You have k lists of sorted integers in ascending order. 
Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Note:
The given list may contain duplicates, so ascending order means >= here.
1 <= k <= 3500
-105 <= value of elements <= 105.
"""

from heapq import *
from collections import defaultdict


class Solution(object):
    def merge_lists(self, nums):
        output = []

        N = sum([len(l) for l in nums])
        K = len(nums)

        heap = []
        pointers = [0] * K

        for i in range(K):
            heappush(heap, (nums[i][0], i))

        for step in range(N):
            element = heappop(heap)
            list_id = element[1]
            output.append(element)
            pointers[list_id] += 1

            if pointers[list_id] < len(nums[list_id]):
                heappush(heap, (nums[list_id][pointers[list_id]], list_id))

        return output

    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        big_list = self.merge_lists(nums)
        N = len(big_list)
        K = len(nums)

        result = (10 ** 6, 0, 0)

        freq = defaultdict(int)

        different = 0
        j = -1
        for i in range(N):
            while j + 1 < N and different < K:
                j += 1
                freq[big_list[j][1]] += 1
                if freq[big_list[j][1]] == 1:
                    different += 1
            # print (i, j, freq)

            if j >= N or different < K:
                break

            assert different == K

            cur_solution = (big_list[j][0] - big_list[i][0], big_list[i][0], big_list[j][0])
            if cur_solution < result:
                result = cur_solution

            freq[big_list[i][1]] -= 1
            if freq[big_list[i][1]] is 0:
                different -= 1

        return [result[1], result[2]]


# custom test case:
nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
s = Solution()
print(s.smallestRange(nums))
