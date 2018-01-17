"""
We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction 
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: 
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

Note:
The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..
"""


class Solution(object):
    res = []

    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stk = []
        for a in asteroids:
            if a > 0:
                stk.append(a)
            else:
                while stk and (stk[-1] > 0) and (abs(a) > stk[-1]):
                    stk.pop()
                if not stk or stk[-1] < 0:
                    stk.append(a)
                elif stk[-1] == abs(a):
                    stk.pop()
        return stk



