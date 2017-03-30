# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str

        chr(65) = 'A'
        chr(65 + 25) = 'Z'
        """

        res = ''
        while n: # cat timp n nu este 0
            res = chr(ord('A') + (n - 1) % 26) + res
            n = (n - 1) / 26
        return res