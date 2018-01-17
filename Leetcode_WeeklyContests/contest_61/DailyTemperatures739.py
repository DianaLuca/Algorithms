"""

"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        res = [0] * n
        stk = []
        for i, temp in enumerate(temperatures):
            if i == 0:
                stk.append((temp, 0))
            while stk and temp > stk[-1][0]:
                res[stk[-1][1]] = i - stk[-1][1]
                stk.pop()
            stk.append((temp, i))
        while stk:
            res[stk[-1][1]] = 0
            stk.pop()
        return res

    def dailyTemperaturesNsquared(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        diffs = [0]*n
        diffs = [0]+[temperatures[_] - temperatures[_ - 1] for _ in range(1, n)]
        for i in range(n):
            j = i+1
            if j < n and diffs[j] - diffs[i] > 0:
                diffs[i] = 1
            else:
                tmpsum = 0
                cnt = 0
                while j < n and tmpsum <= 0:
                    tmpsum += diffs[j]
                    cnt += 1
                    j += 1
                if tmpsum <= 0:
                    diffs[i] = 0
                else:
                    diffs[i] = cnt
        return diffs