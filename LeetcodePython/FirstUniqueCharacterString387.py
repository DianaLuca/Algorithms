# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

from collections import defaultdict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = defaultdict(int)
        for c in s:
            d[c] += 1

        for i, x in enumerate(s):
            if d[x] == 1:
                return i

        return -1


S = Solution()
assert S.firstUniqChar("aba") == 1
assert S.firstUniqChar("abc") == 0