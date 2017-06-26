# Given a positive integer num, write a function which returns
# True if num is a perfect square else False.
# Note: Do not use any built-in library function such as sqrt.
#  Example 1:
# Input: 16
# Returns: True
#  Example 2:
# Input: 14
# Returns: False

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 0, num
        while l < r:
            m = l + (r-l)//2
            if m ** 2 == num:
                return True
            elif m ** 2 > num:
                r = m
            else:
                l = m + 1
        return True if l == num else False

