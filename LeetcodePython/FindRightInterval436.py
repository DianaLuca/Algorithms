# Given a set of intervals, for each of the interval i, check if there exists an interval j
# whose start point is bigger than or equal to the end point of the interval i,
# which can be called that j is on the "right" of i.
# For any interval i, you need to store the minimum interval j's index,
# which means that the interval j has the minimum start point to build the "right" relationship
# for interval i. If the interval j doesn't exist, store -1 for the interval i.
# Finally, you need output the stored value of each interval as an array.
#
# Note:
# You may assume the interval's end point is always bigger than its start point.
# You may assume none of these intervals have the same start point.

import bisect


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """

        ordered_start_pos_tuple = []
        start_list = []

        for i, interval in enumerate(intervals):
            ordered_start_pos_tuple.append((interval.start, i))
            start_list.append(interval.start)

        start_list.sort()
        ordered_start_pos_tuple.sort()
        n = len(ordered_start_pos_tuple)

        res = []
        for interval in intervals:
            index = bisect.bisect_left(start_list, interval.end, 0, n)
            if index == n:
                res.append(-1)
            else:
                res.append(ordered_start_pos_tuple[index][1])

        return res
