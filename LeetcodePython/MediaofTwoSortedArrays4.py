# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).


class Solution(object):
    # TO DO in O(log(m+n))

    # Solution in O(n+m)
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1, n2 = len(nums1), len(nums2)
        midpos = (n1 + n2) // 2

        i, j, res0, res1 = 0, 0, 0, 0
        for _ in range(midpos + 1):
            if i < n1 and j < n2 and nums1[i] <= nums2[j]:
                res0 = res1
                res1 = nums1[i]
                i += 1
            elif i < n1 and j < n2 and nums1[i] > nums2[j]:
                res0 = res1
                res1 = nums2[j]
                j += 1
            elif i == n1 and j < n2:
                res0 = res1
                res1 = nums2[j]
                j += 1
            elif j == n2 and i < n1:
                res0 = res1
                res1 = nums1[i]
                i += 1

        if (n1 + n2) % 2 == 1:
            return res1
        else:
            return (res0 + res1) / 2.0

    # Solution in O(n+m)
    def findMedianSortedArrays(self, nums1, nums2):
        """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: float
        """
        n, m = len(nums1), len(nums2)
        l = nums1 + nums2
        l.sort()  # in O(n+m)
        return l[(n + m) >> 1] if (n + m) % 2 == 1 else (l[(n + m) >> 1] + l[((n + m) >> 1) - 1]) / 2.0