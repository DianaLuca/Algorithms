# Fibonacci with memoization


class Solution(object):
    cache = {}

    def fibo(self, n):
        if n in self.cache:
            return self.cache[n]
        result = 0
        if n <= 1:
            result = 1
        else:
            result = self.fibo(n-2) +\
                     self.fibo(n-1)
        self.cache[n] = result
        return result

s = Solution()
print(s.fibo(40))
