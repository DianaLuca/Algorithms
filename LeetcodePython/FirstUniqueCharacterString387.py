# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()

        for c in s:
            d[c] = d.get(c, 0) + 1

            # if c in d.keys():
            #     val = d.get(c)
            #     d[c] = val + 1
            # else :
            #     d[c] = 1

        i = 0
        while i < len(s):
            if d[s[i]] == 1:
                return i
            else:
                i += 1

        return -1