# There is a list of sorted integers from 1 to n. Starting from left to right,
# remove the first number and every other number afterward until you reach the end of the list.
# Repeat the previous step again, but this time from right to left,
# remove the right most number and every other number from the remaining numbers.
# We keep repeating the steps again, alternating left to right and right to left,
# until a single number remains.
# Find the last number that remains starting with a list of length n.

# Input:
# n = 9,
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8
# 2 6
# 6
#
# Output:
# 6


class Solution(object):
    def rec(self, N, orientation):
        if N == 1:
            return 1
        if orientation == '->':
            print('->', N)
            return self.rec(N // 2, '<-') * 2
        else:
            if N % 2 == 0:
                print('<-', N)
                return (self.rec(N // 2, '->') - 1) * 2 + 1
            else:
                print('<-', N)
                return self.rec(N // 2, '->') * 2

    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        print('start:', n)
        if n == 1:
            return 1
        return self.rec(n, '->')

