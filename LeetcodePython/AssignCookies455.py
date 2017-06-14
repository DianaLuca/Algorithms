# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie.
# Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with;
# and each cookie j has a size sj.
# If sj >= gi, we can assign the cookie j to the child i, and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.
#
# Note:
# You may assume the greed factor is always positive.
# You cannot assign more than one cookie to one child.

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int] kids
        :type s: List[int] cookies
        :rtype: int
        """
        g.sort()
        s.sort()
        ans = 0
        j = 0

        for i in range(len(g)):
            while j < len(s) and g[i] > s[j]:
                j += 1
            if j < len(s) and g[i] <= s[j]:
                ans += 1
                j += 1

        return ans