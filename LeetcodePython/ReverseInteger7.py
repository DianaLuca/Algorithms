# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        strnr = str(x)
        nrofminus = 0
        i = 0
        while i < len(strnr):
            if strnr[i] == '-':
                nrofminus += 1
                i += 1
            elif strnr[i] == '+':
                i += 1
            else:
                break
        inverse = strnr[i:][::-1]
        z = 0
        while z < len(inverse):
            if inverse[z] == '0':
                z += 1
            else:
                break

        if nrofminus % 2 == 1:
            if -int(inverse[z:]) < -2147483648:
                return 0
            return -int(inverse[z:])
        else:
            if inverse[z:] == '':
                return 0
            elif int(inverse[z:]) > 2147483647:
                return 0
            return int(inverse[z:])