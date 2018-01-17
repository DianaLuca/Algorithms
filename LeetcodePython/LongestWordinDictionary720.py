"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
"""


class Solution(object):
    def longestWord_generator(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        word_exists = set(words)
        len_words = sorted([(-len(w), w) for w in words])
        for l, w in len_words:  # O(N)
            if all((w[:i + 1] in word_exists for i in range(-l - 1))):
                return w
        return ''

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        max_len, res_w = 0, ""
        word_exists = set(words)
        for w in word_exists:
            # print w
            cond = True
            for i in range(len(w)):
                if w[:i + 1] not in word_exists:
                    cond = False
                    break
            if cond and len(w) > max_len:
                res_w = w
                max_len = len(w)
            elif cond and len(w) == max_len:
                if w < res_w:
                    res_w = w
        return res_w
