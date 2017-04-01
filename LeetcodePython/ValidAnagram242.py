# Given two strings s and t, write a function to determine if t is an anagram of s.


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_lst = list(s)
        s_lst.sort()
        t_lst = list(t)
        t_lst.sort()

        return (s_lst == t_lst)
