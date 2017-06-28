# Follow up for H-Index274.py: What if the citations array is sorted in ascending order?
# Could you optimize your algorithm?


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        n = len(citations)
        l = 0
        r = n - 1

        while l <= r:
            med = (l + r) // 2
            if citations[med] == n - med:
                return n - med
            elif citations[med] > n - med:
                r = med - 1
            else:
                l = med + 1
        return n - l