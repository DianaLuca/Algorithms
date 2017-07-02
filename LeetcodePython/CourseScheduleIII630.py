# There are n different online courses numbered from 1 to n.
# Each course has some duration(course length) t and closed on dth day.
# A course should be taken continuously for t days and must be finished before or on the dth day.
# You will start at the 1st day.
#
# Given n online courses represented by pairs (t,d), your task is to
# find the maximal number of courses that can be taken.


from heapq import heappush, heappop


class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """

        courses.sort(key=lambda x: x[1])
        # [[100, 200], [1000, 1250], [200, 1300], [2000, 3200]]

        hq = []  # heap queue -> also known as the priority queue
        summ = 0

        for i, course in enumerate(courses):
            summ += course[0]
            heappush(hq, -course[0])
            while summ > course[1]:
                summ += heappop(hq)
        return len(hq)
