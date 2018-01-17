"""
N = 5:

* * * * *
- - - - *
* * * - *
* - - - *
* * * * *


"""

from collections import namedtuple

Point = namedtuple('Point', ('row', 'col'))


def inMatrix(pos, N):
    """ Checks if point pos in is the matrix """
    return pos.row >= 0 and pos.row < N and pos.col >= 0 and pos.col < N


def advance(pos, delta):
    """ Moves pos one step in the direction of delta """
    return Point(pos.row + delta.row, pos.col + delta.col)


def printSpiral(N):
    # dirs = right, down, left, up
    dirs = [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]
    matrix = [[-1] * N for _ in range(N)]

    pos = Point(0, 0)
    d = 0  # to the right

    for step in range(N * N):
        matrix[pos.row][pos.col] = step
        npos = advance(pos, dirs[d])
        if inMatrix(npos, N) and matrix[npos.row][npos.col] == -1:
            pos = npos
        else:
            d = (d + 1) % 4
            pos = advance(pos, dirs[d])

    for row in matrix:
        tokens = ["{0: <3}".format(el) for el in row]
        print(''.join(tokens))


#printSpiral(4)


def main():
    printSpiral(5)
    print("\n")
    printSpiral(6)

if __name__ == main():
    main()
