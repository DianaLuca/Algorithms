class Solution(object):
    def baseTwo(self, n):
        x = n
        n = abs(n)
        k = []
        while n > 0:
            a = int(n % 2)
            k.append(a)
            n = (n-a) / 2

        result = ""
        if x < 0:
            result += "-"
        for j in k[::-1]:
            result += str(j)
        return result


    def baseSeven(self, n):
        k = []
        x = n
        n = abs(n)
        while n > 0:
            modseven = int(n % 7)
            k.append(modseven)
            n = (n - modseven) / 7

        result = ""
        if x < 0:
            result += "-"
        for i in k[::-1]:
            result += str(i)
        return result

s = Solution()
print(s.baseTwo(23))  # "10111"
print(s.baseSeven(-26))  # "-35"
