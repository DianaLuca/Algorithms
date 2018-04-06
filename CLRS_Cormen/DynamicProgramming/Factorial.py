# factorial with memoization
class Solution(object):

    def factorial_tabulation(self, x):
        dp = [-1 for _ in range(x+1)]
        dp[0] = 1

        for i in range(1, x+1):
            dp[i] = i * dp[i-1]
        return dp[x]


    def factorial_memoization(self, n):
        # returns factorial n!

        dp = [-1 for i in range(n+1)]

        if n == 0:
            return 1
        if dp[n] == -1:
            dp[n] = n * self.factorial(n-1)
        return dp[n]


s = Solution()
n = 3
print(n,"! = ",s.factorial_tabulation(n))
