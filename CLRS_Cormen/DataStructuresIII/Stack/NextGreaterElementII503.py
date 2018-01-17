"""
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.

Note: The length of given array won't exceed 10000.
"""


class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [0] * n

        stk = []
        for i in range(2 * n - 1, -1, -1):
            while (stk and nums[stk[-1]] <= nums[i % n]):
                stk.pop()
            res[i % n] = -1 if not stk else nums[stk[-1]]
            stk.append(i % n)
        print(stk)
        return res

    def nextGreaterElementsTLE(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []

        for i, num in enumerate(nums):
            j = i + 1
            while True:
                if j == i:
                    res.append(-1)
                    break
                elif j == n:
                    j = 0
                    continue
                elif nums[j] > num:
                    res.append(nums[j])
                    break
                j += 1
                # print(res)

        return res
