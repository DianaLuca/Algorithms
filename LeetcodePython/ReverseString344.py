# Write a function that takes a string as input and returns the string reversed.

class Solution(object):
    def reverseString(self, s):
        if len(s) <= 1:
            return s
        return s[::-1]