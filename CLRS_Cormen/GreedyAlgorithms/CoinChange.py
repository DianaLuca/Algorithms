"""
You are given unlimited nr of coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        m = amount + 1
        n = len(coins)
        dp = [m for _ in range(m)]
        dp[0] = 0

        for i in range(1, m):
            for j in range(n):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return dp[amount] if dp[amount] <= amount else -1


#test
coins = [1, 2, 5]
amount = 11
s = Solution()

print(s.coinChange(coins, amount))
