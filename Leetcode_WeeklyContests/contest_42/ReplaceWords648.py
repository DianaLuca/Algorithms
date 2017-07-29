"""
In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. 
For example, the root an, followed by other, which can form another word another.
Now, given a dictionary consisting of many roots and a sentence. 
You need to replace all the successor in the sentence with the root forming it. 
If a successor has many roots can form it, replace it with the root with the shortest length.
You need to output the sentence after the replacement.

Example 1:
Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Note:
The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000
"""

import collections


class Solution(object):
    def replaceWords(self, roots, sentence):
        root_set = set(roots)

        def replace(word):
            n = len(word)
            for i in range(1, n):
                if word[:i] in root_set:
                    return word[:i]
            return word

        sentence_words = sentence.split()
        new_sentence = " ".join(map(replace, sentence_words))
        return new_sentence

    def replaceWords_trie(self, roots, sentence):
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        END = True
        for root in roots:
            cur = trie
            for letter in root:
                cur = cur[letter]
            cur[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur: break
                cur = cur[letter]
                if END in cur:
                    return cur[END]
            return word

        sentence_words = sentence.split()
        new_sentence = " ".join(map(replace, sentence_words))
        print(new_sentence)
        return new_sentence
        # return " ".join(map(replace, sentence.split()))

s = Solution()
s.replaceWords_trie(["cat", "bat", "rat"], "the cattle was rattled by the battery")