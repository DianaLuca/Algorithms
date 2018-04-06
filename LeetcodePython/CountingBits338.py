"""
Given a non negative integer number num For every numbers i in the range 0 ≤ i ≤ num 
calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). 
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

"""

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # O(N)
        res = [0, 1]
        while len(res) < num + 1:
            res += [_ + 1 for _ in res]
        return res[:num + 1]


    def countB(self, num):
        res = []
        for i in range(num+1):
            crr = bin(i)[2:]
            cnt = 0
            for ch in crr:
                if ch == "1":
                    cnt+=1
            res.append(cnt)
        return res