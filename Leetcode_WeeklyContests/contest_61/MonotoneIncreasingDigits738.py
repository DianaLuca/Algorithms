"""
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.
(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)
Example 2:
Input: N = 1234
Output: 1234

Example 1:
Input: N = 10
Output: 9

Example 3:
Input: N = 332
Output: 299

Note: N is an integer in the range [0, 10^9].
"""


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int : 1333219
        :rtype: int
        """
        if N < 10:
            return N

        n, inv_index = N, -1
        num = [int(d) for d in str(n)[::-1]]
        # num = [9,1,2,3,3,3,1]

        for i in range(1, len(num)):  # i: [1 -> 6]
            if num[i] > num[i - 1] or (inv_index != -1 and num[inv_index] == num[i]):
                inv_index = i  # inv_index: -1 <init>, 2, 3, 4, 5

        if inv_index == -1: return N

        # num: [9, 1, 2, 3, 3, 3, 1]
        # inv_index: 5
        for i in range(inv_index):  # i: [0 -> 4]
            num[i] = 9
        num[inv_index] -= 1

        # num = [9, 9, 9, 9, 9, 2, 1]
        return int(''.join([str(i) for i in num[::-1]]))