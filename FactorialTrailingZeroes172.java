package LeetCodeAlgorithms;

/**
 * Given an integer n, return the number of trailing zeroes in n!.
 * Note: Your solution should be in logarithmic time complexity.
 *
 * Created by dianaluca on 10/6/16.
 */

public class FactorialTrailingZeroes172 {
  public int trailingZeroes(int n) {
    int res = 0;

    while (n != 0) {
      n /= 5;  // complexity: O(log5) logarithm base 5
      res += n; // how many five's contains n.
    }

    return res;
  }
}
