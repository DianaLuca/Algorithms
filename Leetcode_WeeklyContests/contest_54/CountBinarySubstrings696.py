"""Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, 
and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters."""



class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        i = 0
        while i < n:
            if s[i] == "1":
                j = i
                cnt = 0
                while j < n and s[j] == "1":
                    cnt += 1
                    j += 1
                cnt2 = 0
                k = j
                while j < n and s[j] == "0":
                    cnt2 += 1
                    j += 1
                res += min(cnt, cnt2)
                # print i, k, j, res
                i = k

            else:  # 0
                j = i
                cnt = 0
                while j < n and s[j] == "0":
                    cnt += 1
                    j += 1
                # print cnt
                cnt2 = 0
                k = j
                while j < n and s[j] == "1":
                    cnt2 += 1
                    j += 1
                res += min(cnt, cnt2)
                # print i, k, j, res
                i = k
        return res