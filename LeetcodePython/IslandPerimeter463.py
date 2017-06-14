# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally).
# The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
# Determine the perimeter of the island.


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # left: grid[i][j-1]
                    if j - 1 < 0:
                        res += 1
                    elif grid[i][j - 1] == 0:
                        res += 1

                    # up: grid[i-1][j]
                    if i - 1 < 0:
                        res += 1
                    elif grid[i - 1][j] == 0:
                        res += 1

                    # right: grid[i][j+1]
                    if j + 1 == len(grid[0]):
                        res += 1
                    elif grid[i][j + 1] == 0:
                        res += 1

                    # down: grid[i+1][j]
                    if i + 1 == len(grid):
                        res += 1
                    elif grid[i + 1][j] == 0:
                        res += 1
        return res
