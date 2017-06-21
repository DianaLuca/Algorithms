# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
# You need to help them find out their common interest with the least list index sum.
# If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

import sys


class Solution(object):
    def findRestaurant(self, list1, list2):
        dictlist1 = {u: i for i, u in enumerate(list1)}
        res = []
        best = 1e9

        for i, el in enumerate(list2):
            val = dictlist1.get(el, 1e9)
            if i + val < best:
                best = i + val
                res = [el]
            elif i + val == best:
                res.append(el)
        return res

    def findRestaurantUglySolution(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1 = {}
        dict2 = {}
        for i, el in enumerate(list1):
            dict1[el] = i
        for i, el in enumerate(list2):
            dict2[el] = dict1.get(el, -sys.maxsize - 1) + i

        res = []
        minval = sys.maxsize
        for key in dict2.keys():
            val = dict2[key]
            if val >= 0:
                minval = min(val, minval)
        for key in dict2.keys():
            if dict2[key] == minval:
                res.append(key)

        return res