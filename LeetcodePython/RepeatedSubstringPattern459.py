# Given a non-empty string check if it can be constructed by taking a substring of it and
# appending multiple copies of the substring together.
# You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(1, n//2 + 1):
            if n % i != 0:
                continue
            if self.is_prefix(s, i):
                return True
        return False

    def is_prefix(self, s, i):
        n = len(s)
        for k in range(n//i):
            if s[:i] != s[k * i:(k + 1) * i]:
                return False
        return True


s = Solution()
print(s.repeatedSubstringPattern("abaacabaac"))  # True
print(s.repeatedSubstringPattern("aba"))  # False
