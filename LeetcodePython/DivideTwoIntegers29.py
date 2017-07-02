# Divide two integers without using multiplication, division and mod operator.
# If it is overflow, return MAX_INT.

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if divisor == 0:
            return -1

        possign = True if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)  else False
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend < divisor:
            return 0

        left = 1
        right = dividend
        while left <= right:
            mid = (left + right) >> 1
            if mid * divisor == dividend:
                if mid == 2147483648 and possign:
                    mid -= 1
                return mid if possign else -mid
            elif mid * divisor < dividend:
                left = mid + 1
            else:  # mid * divisor > dividend:
                right = mid - 1

        if possign:
            left = left if left* divisor <= dividend else left - 1
            if left == 2147483648:
                left -= 1
        else:
            left = -left if left * divisor <= dividend else -left + 1
        return left
