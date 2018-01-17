"""
Query in O(1) the minimum element from a given range from a given array A

"""
from copy import copy

class RMQ(object):
    # precalculate RangeMinQueue data structure
    def precompute(self, A):
        self.n = len(A)
        self.level = self._two_power(self.n)
        self.lookup = [[0 for _ in range(self.n)] for _ in range(self.level+1)]

        for lvl in range(self.level+1):
            if lvl == 0:
                self.lookup[0] = A
            else:
                block = 2**lvl
                for i in range(self.n - block + 1):
                    self.lookup[lvl][i] = min(self.lookup[lvl-1][i], self.lookup[lvl-1][i + block//2])

        print(self.lookup)

    # query RMQ in O(1) time complexity
    def query_interval(self, left, right):
        m = right - left + 1
        pwr = self._two_power(m)
        return min(self.lookup[pwr][left], self.lookup[pwr][right - 2**pwr + 1])

    # helper: calculate the biggest power of 2 smaller or equal than a given number
    def _two_power(self, n):
        pwr = 1
        res = 2
        while res <= n:
            res *= 2
            pwr += 1
        return pwr-1


s = RMQ()
A = [12, 7, 8, 2, 1, 9, 4, 0]
s.precompute(A)

print(s.query_interval(0,1))  # 7
print(s.query_interval(1,5))  # 1
print(s.query_interval(2,2))  # 8
print(s.query_interval(0,7))  # 1

#print(s._two_power(4))