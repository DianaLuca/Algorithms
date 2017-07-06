# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []

        k = sorted(intervals, key=lambda i: i.start)
        res = [k[0]]
        for i in range(1, len(k)):
            temp = res[-1]
            if temp.end < k[i].start:
                res.append(k[i])
            else:
                if temp.end < k[i].end:
                    res[-1].end = k[i].end
        return res
