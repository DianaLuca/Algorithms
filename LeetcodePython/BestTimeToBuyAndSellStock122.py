# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).

import sys


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        profit = 0
        for i in range(1, n):
            dif = prices[i] - prices[i - 1]
            if dif > 0:
                profit += dif
        return profit


s = Solution()
print(s.maxProfit([5,4,3,2,1]))
print(s.maxProfit([1,2,4]))