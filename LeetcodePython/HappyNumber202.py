# Write an algorithm to determine if a number is "happy".
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#  Those numbers for which this process ends in 1 are happy numbers.



class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmpl = str(n)
        preSet = set()

        while True:
            res = 0
            for el in tmpl:
                res += int(el) * int(el)
            if res == 1:
                return True
            if res in preSet:
                return False
            preSet.add(res)
            tmpl = str(res)