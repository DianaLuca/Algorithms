"""
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). 
The string represents the key and the integer represents the value. 
If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' 
value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
"""


class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here
        """
        self.mapsum = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.mapsum[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        n = len(prefix)
        ressum = 0
        for key in self.mapsum.keys():
            if key[:n] == prefix:  # if key.startswith(prefix):
                ressum += self.mapsum[key]
        return ressum

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
