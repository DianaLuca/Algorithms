# Given a non-empty array of integers, return the third maximum number in this array.
# If it does not exist, return the maximum number. The time complexity must be in O(n).
# Example 1:
# Input: [3, 2, 1]
# Output: 1
#
# Explanation: The third maximum is 1.
# Example 2:
# Input: [1, 2]
# Output: 2
#
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: [2, 2, 3, 1]
# Output: 1
#
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.

import sys


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = -sys.maxsize
        max_nd = -sys.maxsize
        max_rd = -sys.maxsize

        for i, el in enumerate(nums):
            if el > max_rd:
                if el > max_nd:
                    if el > max:
                        max_rd = max_nd
                        max_nd = max
                        max = el
                    elif el == max:
                        continue
                    else:
                        max_rd = max_nd
                        max_nd = el

                elif el == max_nd:
                    continue
                else:
                    max_rd = el

        if max_rd == -sys.maxsize:
            return max
        return max_rd

