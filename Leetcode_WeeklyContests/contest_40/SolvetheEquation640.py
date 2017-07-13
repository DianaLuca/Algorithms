# Solve a given equation and return the value of x in the form of string "x=#value".
# The equation contains only '+', '-' operation, the variable x and its coefficient.
#
# If there is no solution for the equation, return "No solution".
#
# If there are infinite solutions for the equation, return "Infinite solutions".
#
# If there is exactly one solution for the equation, we ensure that the value of x is an integer.
#
# Example 1:
# Input: "x+5-3+x=6+x-2"
# Output: "x=2"


class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left, right = equation.split("=")

        left_poly = self.find_polynomial(left)
        right_poly = self.find_polynomial(right)

        for i in range(2):
            left_poly[i] -= right_poly[i]
        print(left_poly)
        if left_poly[0] == 0:
            if left_poly[1] == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x={}".format(-left_poly[1] / left_poly[0])

    def find_polynomial(self, expr):
        if expr[0] != '-':
            expr = '+' + expr

        result = [0, 0]
        for i, c in enumerate(expr):
            if c == '-' or c == '+':
                token = ''
                j = i + 1
                while j < len(expr) and expr[j] != '+' and expr[j] != '-':
                    token += expr[j]
                    j += 1
                print(c, token)
                if token[-1] == 'x':
                    if len(token) > 1:
                        value = int(token[:-1])
                    else:
                        value = 1
                    if c == '+':
                        result[0] += value
                    else:
                        result[0] -= value
                else:
                    value = int(token)
                    if c == '+':
                        result[1] += value
                    else:
                        result[1] -= value

            i = j - 1
        return result

        # def find_polynomial2(self, expr):
        #   operators = []
        #   tokens = []
        #   if expr[0] != '-':
        #       expr = '+' + expr

        #   for i in range(len(expr)):
        #       if expr[i] == '-' or expr[i] == '+':
        #           operators.append(expr[i])
        #       expr = expr.replace('+', ' ')
        #       expr = expr.replace('-', ' ')
        #   print (expr)
        #   tokens = expr.split()
        #   print (operators, tokens)
