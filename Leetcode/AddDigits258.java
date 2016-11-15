package Algorithms.Leetcode;

/**
 * Given a non-negative integer num,
 * repeatedly add all its digits until the result has only one digit.

 * For example:
 * Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2.
 * Since 2 has only one digit, return it.

 * Follow up:
 * Could you do it without any loop/recursion in O(1) runtime?

 * Created by dianaluca on 9/15/16.
 */

public class AddDigits258 {
  public static int addDigits(int num) {
    int sum = 0;
    while (num > 0) {
      System.out.printf("Add digit: %d while %d is bigger than 0 \n", (num % 10), num);
      sum += num % 10;
      num /= 10;
    }

    if (sum >= 10) {
      System.out.printf("sum_of_digits = %d >= 10, repeat recursively the process " +
          "till the sum is less than 10! \n", sum);
      return addDigits(sum);
    }
    return sum;
  }

  public static void main(String[] args){
    int N = 1234;
    int res = addDigits(N);
    System.out.printf("sum of %d's digits is: %d", N, res);
  }
}
