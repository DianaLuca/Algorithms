# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def valueOf(self, rom):
        if (rom == 'I'):
            return 1
        if (rom == 'V'):
            return 5
        if (rom == 'X'):
            return 10
        if (rom == 'L'):
            return 50
        if (rom == 'C'):
            return 100
        if (rom == 'D'):
            return 500
        if (rom == 'M'):
            return 1000
        return -1

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0

        while (i < len(s)):
            # Getting value of symbol s[i]
            chVal1 = self.valueOf(s[i])

            if i < len(s) - 1:
                chVal2 = self.valueOf(s[i + 1])
                if chVal1 >= chVal2:
                    res += chVal1
                    i += 1
                else:
                    res += chVal2 - chVal1
                    i += 2
            else:
                res += chVal1
                i += 1

        return res