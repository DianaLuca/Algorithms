package Algorithms.related;

import java.util.Scanner;

/**
 * Created by dianaluca on 12/3/16.
 */
public class SpiderDynamicP {
  public static long[][] Web;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Introduce #lines and #columns");
    int line = sc.nextInt();
    int col = sc.nextInt();
    Web = new long[line+1][col+1];
    for (int  i = 0; i <= line; i++) {
      for (int j = 0; j <= col; j++) {
        Web[i][j] = -1;
      }
    }

    //System.out.println("Recursively: " + recursiveSolution(line, col));
    System.out.println("Using memoization: " + memoization2(line, col));
  }

  /**
   * Input:
   * 7
   * 11
   *
   * Output:
   * 31824
   */

  public static long solution(int line, int col) {
    if(line == 0 && col == 0) return 1;
    long[][] values = new long[line][col];

    for (int i = 0; i < line; i++) {
      for (int j = 0; j < col; j++) {
        if (i == 0) values[i][j] = j + 2;
        else if (j == 0) values[i][j] = i + 2;
        else {
          values[i][j] = values[i-1][j] + values[i][j-1];
        }
      }
    }
    return values[line-1][col-1];
  }

  public static long memoization(int line, int col) {
    // if (col == 0 && line == 0) return 0;
    if (Web[line-1][col-1] != -1) return Web[line-1][col-1];
    if (col == 1 && line == 1) return Web[line-1][col-1] = 2;
    if (col == 1) return Web[line-1][col-1] = line + 1;
    if (line == 1) return Web[line-1][col-1] = col + 1;
    return memoization(line-1, col) + memoization(line, col-1);
  }

  public static long memoization2(int line, int col) {
    // 1. Base case
    if (line == 0 && col == 0) return 1;

    // 2. Check if it's already computed
    if (Web[line][col] != -1)
      return Web[line][col];

    // 3. If not, we need to compute it
    long result = 0;

    // These are the exactly the lines for the recursion
    if (line >= 1) result += memoization2(line - 1, col);
    if (col >= 1) result += memoization2(line, col - 1);

    // At this point, the result for these parameters (line, col) is computed forever
    return Web[line][col] = result;
  }

  public static long recursiveSolution(int line, int col) {
    if (col == 0 && line == 0) return 1;
    if (col == 1 && line == 1) return 2;
    if (col == 1) return line + 1;
    if (line == 1) return col + 1;
    return recursiveSolution(line-1, col) + recursiveSolution(line, col-1);
  }

  public static long quadraticGrid(int N) {
    long paths = 1;

    for(int i = 0; i < N; i++) {
      paths *= (2 * N) - i;
      paths /= i + 1;
    }
    return paths;
  }
}
