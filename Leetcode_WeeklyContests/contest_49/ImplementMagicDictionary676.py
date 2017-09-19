"""
Implement a magic directory with buildDict, and search methods.
For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.
For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character
in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:
You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. 
You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, 
as static/class variables are persisted across multiple test cases.
"""
from collections import defaultdict


class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = defaultdict(list)

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :param dict: List[str]
        :return: void
        """
        for word in dict:
            self.dictionary[len(word)].append(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :param word: str
        :return: bool
        """
        if len(self.dictionary[len(word)]) == 0:
            return False  # word is not in dictionary

        for eachword in self.dictionary[len(word)]:
            diff = 0
            for i in range(len(word)):
                if eachword[i] != word[i]:
                    diff += 1
            if diff == 1:
                return True

        return False
