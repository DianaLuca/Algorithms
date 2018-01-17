"""
Count the number of prime numbers less than a non-negative number, n
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        if n == 3:
            return 1

        isPrime = [True] * (n)
        isPrime[0] = False
        isPrime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            #print(isPrime, i, count)
            if isPrime[i]:
                p = i + i
                while p < n:
                    #print("for in for",i, j)
                    isPrime[p] = False
                    p += i
        return sum(isPrime)


def main():
    s = Solution()
    print(s.countPrimes(2))
    print(s.countPrimes(3))
    print(s.countPrimes(4))
    print(s.countPrimes(5))
    print(s.countPrimes(6))
    print(s.countPrimes(499979))

if __name__ == main():
    main()