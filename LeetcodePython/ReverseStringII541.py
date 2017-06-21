# Given a string and an integer k, you need to reverse the first k characters
# for every 2k characters counting from the start of the string.
# If there are less than k characters left, reverse all of them.
# If there are less than 2k but greater than or equal to k characters,
# then reverse the first k characters and left the other as original.

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        j = 0
        i = j + k
        while j < n and i < n:
            if n-i-1 < k:
                s = s[:j] + ''.join(reversed(s[j::]))
                break
            elif n-i-1 < 2*k and n-i-1 >= k:
                s = s[:j] + ''.join(reversed(s[j:i])) + s[i:]
                j = i
                i += k
            else:
                s = s[:j] + ''.join(reversed(s[j:i])) + s[i:]
                j = i
                i += k
        return s