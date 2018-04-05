"""
A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.

Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
"""


class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        nrx = sum(line.count('X') for line in board)
        nro = sum(line.count('O') for line in board)

        if nrx < nro:
            return False
        if nrx >= nro:
            if nrx - nro > 1:
                return False

        # Verify the terminal condition of winning (8 posibilities: 3 lines, 3 columns, 2 diagonals)
        def win(board, player):
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
                if all(board[j][i] == player for j in range(3)):
                    return True
            return (player == board[1][1] == board[0][0] == board[2][2] or
                    player == board[1][1] == board[0][2] == board[2][0])

        if win(board, 'X') and nrx != nro + 1:
            return False
        if win(board, 'O') and nrx != nro:
            return False

        return True