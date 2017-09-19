"""
nitially, there is a Robot at position (0, 0). 
Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. 
The valid robot moves are R (Right), L (Left), U (Up) and D (down). 
The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if len(moves) % 2 != 0:
            return False
        res = 0
        for ch in moves:
            if ch == "U":
                res += 10
            if ch == "D":
                res -= 10
            if ch == "L":
                res -= 1
            if ch == "R":
                res += 1
        if res == 0:
            return True
        else:
            return False

    def judgeCircle_fastest(self, moves):
        return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")