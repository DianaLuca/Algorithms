package Algorithms.Leetcode;

/**
 * Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.
 *
 * Note:
 * The length of both num1 and num2 is < 5100.
 * Both num1 and num2 contains only digits 0-9.
 * Both num1 and num2 does not contain any leading zero.
 * You must not use any built-in BigInteger library or convert the inputs to integer directly.
 *
 * Created by dianaluca on 10/12/16.
 */

public class AddStrings415 {
  public String addStrings(String num1, String num2) {
    int i, j;
    i = num1.length() - 1;
    j = num2.length() - 1;
    StringBuilder sum = new StringBuilder();
    int tmp = 0;

    while (i >= 0 || j >= 0) {
      if (i >= 0 && j >= 0) {
        tmp += (num1.charAt(i) - '0') + (num2.charAt(j) - '0');
        if (tmp < 10) sum.append(tmp);
        else sum.append(tmp % 10);
        tmp /= 10;
        i--;
        j--;
      }
      if (i >= 0 && j < 0) {
        tmp += num1.charAt(i) - '0';
        if (tmp < 10) sum.append(tmp);
        else sum.append(tmp % 10);
        tmp /= 10;
        i--;
      }
      if (j >= 0 && i < 0) {
        tmp += num2.charAt(j) - '0';
        if (tmp < 10) sum.append(tmp);
        else sum.append(tmp % 10);
        tmp /= 10;
        j--;
      }
    }
    if (tmp != 0) sum.append(tmp);

    return sum.reverse().toString();
  }
}
