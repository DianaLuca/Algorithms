# Write a function to find the longest common prefix string amongst an array of strings.

import sys

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        res = ""
        if not strs:
            return res

        minlen = sys.maxsize
        for el in strs:
            if len(el) < minlen:
                minlen = len(el)
                small = el

        for i in range(len(small)):
            for j in range(len(strs)):
                if strs[j][i] != small[i]:
                    return res
                if j == len(strs) - 1 and strs[j][i] == small[i]:
                    res += small[i]

        return res