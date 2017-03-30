class Solution(object):
    def getSum(self, x, y):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        while y is not 0:
            carry = x & y
            print("carry = %d") % carry
            x = x ^ y
            print("x = %d") % x
            y = carry << 1
            print("y = %d") % y
        return x