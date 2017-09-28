"""
Given a 2D integer matrix M representing the gray scale of an image, 
you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) 
of all the 8 surrounding cells and itself. 
If a cell has less than 8 surrounding cells, then use as many as you can.

Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
"""


class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(M)
        m = len(M[0])
        R = [[-1 for i in range(m)] for j in range(n)]

        if n <= 1 and m <= 1:
            return M

        if n == 1:
            i = 0
            for j in range(m):
                if j == 0:
                    R[i][j] = (M[i][j] + M[i][j + 1]) / 2
                elif j == m - 1:
                    R[i][j] = (M[i][j] + M[i][j - 1]) / 2
                else:
                    R[i][j] = (M[i][j] + M[i][j - 1] + M[i][j + 1]) / 3
            return R

        if m == 1:
            j = 0
            for i in range(n):
                if i == 0:
                    R[i][j] = (M[i][j] + M[i + 1][j]) / 2
                elif i == n - 1:
                    R[i][j] = (M[i][j] + M[i - 1][j]) / 2
                else:
                    R[i][j] = (M[i][j] + M[i - 1][j] + M[i + 1][j]) / 3
            return R

        for i in range(n):
            for j in range(m):
                if i == 0:
                    if j == 0:
                        R[i][j] = (M[i][j] + M[i + 1][j] + M[i + 1][j + 1] + M[i][j + 1]) / 4
                    elif j == m - 1:
                        R[i][j] = (M[i][j] + M[i + 1][j] + M[i + 1][j - 1] + M[i][j - 1]) / 4
                    else:
                        R[i][j] = (M[i][j] + M[i + 1][j] + M[i + 1][j + 1] + M[i][j + 1] + M[i][j - 1] + M[i + 1][
                            j - 1]) / 6
                elif i == n - 1:
                    if j == 0:
                        R[i][j] = (M[i][j] + M[i - 1][j] + M[i - 1][j + 1] + M[i][j + 1]) / 4
                    elif j == m - 1:
                        R[i][j] = (M[i][j] + M[i][j - 1] + M[i - 1][j - 1] + M[i - 1][j]) / 4
                    else:
                        R[i][j] = (M[i][j] + M[i][j - 1] + M[i][j + 1] + M[i - 1][j - 1] + M[i - 1][j] + M[i - 1][
                            j + 1]) / 6
                else:
                    if j == 0:
                        R[i][j] = (M[i][j] + M[i - 1][j] + M[i - 1][j + 1] + M[i][j + 1] + M[i + 1][j + 1] + M[i + 1][
                            j]) / 6
                    elif j == m - 1:
                        R[i][j] = (M[i][j] + M[i][j - 1] + M[i - 1][j - 1] + M[i - 1][j] + M[i + 1][j - 1] + M[i + 1][
                            j]) / 6
                    else:
                        R[i][j] = (M[i][j] + M[i][j - 1] + M[i][j + 1] + M[i - 1][j - 1] + M[i - 1][j] + M[i - 1][
                            j + 1] + M[i + 1][j - 1] + M[i + 1][j] + M[i + 1][j + 1]) / 9
        return R