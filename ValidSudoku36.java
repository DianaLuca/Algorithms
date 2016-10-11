package LeetCodeAlgorithms;

import java.util.HashSet;
import java.util.Set;

/**
 * Determine if a Sudoku is valid according to Sudoku Puzzles Rules:
 * 1: Each row must have the numbers 1-9 occuring just once;
 * 2: Each column must have the numbers 1-9 ocurring just once;
 * 3: The numbers 1-9 must occur just once in each of the 9 sub-boxes of the grid.
 *
 * The Sudoku board could be partially filled, where empty cells are filled with '.' char
 *
 * Created by dianaluca on 10/11/16.
 */

public class ValidSudoku36 {
  public boolean isValidSudoku (char[][] board) {
    int[][] row = new int[9][9];
    int[][] col = new int[9][9];
    int[][][] miniBox = new int[3][3][9];

    for (int i = 0; i < 9; i++) {
      for (int j = 0; j < 9; j++) {
        if (board[i][j] == '.') {
          continue;
        } else {
          int index = board[i][j];
          row[i][index] += 1;
          if (row[i][index] > 1) return false;
          col[j][index] += 1;
          if (col[j][index] > 1) return false;
          miniBox[i/3][j/3][index] += 1;
          if (miniBox[i/3][j/3][index] > 1) return false;
        }
      }
    }
    return true;
  }

  /**
   * Solution 2: Using HashSet:
   * encode as strings the set of things we visit, like this:
   * '4' in row 7 is encoded as "(4)7".
   * '4' in column 7 is encoded as "7(4)".
   * '4' in the top-right block is encoded as "0(4)2".
   * It's remarkable that each element would be unique after this encoding.
   *
   * return false if the visited characters are already added in set
   */

  public boolean isValidSudoku2(char[][] board) {
    Set<String> already = new HashSet<String>();

    for (int i = 0; i < 9; i++) {
      for (int j = 0; j < 9; j++) {
        if (board[i][j] == '.') continue;
        else  {
          String el = "(" + board[i][j] + ")";
          if ( !already.add(el + i) ||
               !already.add(j + el) ||
               !already.add(i/3 + el + j/3))
              return false;
        }
      }
    }
    return true;
  }
}
