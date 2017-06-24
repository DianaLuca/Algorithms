# You are given a string representing an attendance record for a student.
# The record only contains the following three characters:
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than
# one 'A' (absent) or more than two continuous 'L' (late).
# You need to return whether the student could be rewarded according to his attendance record.


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # cha <= 1, chl <= 2 continuous
        cha = 0
        for i,ch in enumerate(s):
            if ch == "A":
                cha += 1
            elif ch == "L":
                if s[i:i+3] == "LLL":
                    return False
        if cha > 1:
            return False
        return True