class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ph in s:
            if ph == "[" or ph == "{" or ph == "(":
                stack.append(ph)
            else:
                if not stack:
                    return False
                peek = stack.pop()
                if ph == ")" and peek == "(":
                    continue
                elif ph == "]" and peek == "[":
                    continue
                elif ph == "}" and peek == "{":
                    continue
                else:
                    return False
        if not stack:
            return True
        return False
