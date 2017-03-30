# Write a function that takes a string as input and returns the string reversed.

class Solution(object):
    def reverseString(self, s):
        l = list(s)
        for i in range(len(l) // 2):
            aux = l[i]
            l[i] = l[len(s) - 1 - i]
            l[len(s) - 1 - i] = aux

        return ''.join(l)

print (Solution().reverseString("abcde"))