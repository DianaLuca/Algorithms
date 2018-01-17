"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u,v) which consists of one element from the first array and one element from the second array
Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3
Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
"""

from heapq import heappush, heappop


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]

        ex: 
        [1,7,11]
        [2,4,6]
        3
        """

        heap = []

        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heappush(heap, [nums1[i] + nums2[j], i, j])

        push(0, 0)
        res = []

        while heap and len(res) < k:
            sm, i, j = heappop(heap)
            res.append([nums1[i], nums2[j]])

            push(i, j + 1)

            if j == 0:
                push(i + 1, 0)
                # print i, j, heap
        return res


def main():
    pass

if __name__ == '__main__':
    main()
