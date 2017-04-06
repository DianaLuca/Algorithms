# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        min = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            else:
                if prices[i] - min > profit:
                    profit = prices[i] - min

        return profit

    #  dynamic programming solution:
    def maxProfitDP(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        minl = sys.maxsize
        profit = 0

        for el in prices:
            minl = min(minl, el)
            profit = max(profit, el - minl)

        return profit