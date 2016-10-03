package LeetCodeAlgorithms;

import java.util.Arrays;

/**
 * Given a non-negative number represented as an array of digits, plus one to the number.
 * The digits are stored such that the most significant digit is at the head of the list.
 *
 * ex1: given: {9,9,9,9} returns: {1,0,0,0}
 * ex2: given: {1,2,3} returns: {1,2,4}
 *
 * Created by dianaluca on 10/3/16.
 */

public class PlusOne66 {
  public static int[] plusOne(int[] digits) {
    int N = digits.length;
    int i = N - 1;

    if (digits[i] != 9) {
      digits[i] = digits[i] + 1;
    } else {
      while (i >= 0 && digits[i] == 9) {
        i--;
      }

      if (i == -1) {
        int[] res = new int[N + 1];
        res[0] = 1;
        for (int j = 1; j <= N; j++){
          res[j] = 0;
        }
        return res;
      }
      else if (i >= 0) {
        digits[i] = digits[i] + 1;
        i++;
        while (i < N) {
          digits[i] = 0;
          i++;
        }
      }
    }
    return digits;
  }

  //Test Client:
  public static void main(String[] args) {
    int[] digitsNine = {9, 9, 9, 9};
    int[] digitsA = {1, 2, 3, 4};
    int[] digitsB = {1, 2, 9, 9};
    System.out.println("all nine " + Arrays.toString(digitsNine) + " plus 1: \n" + Arrays.toString(plusOne(digitsNine)));
    System.out.println("digitsA " + Arrays.toString(digitsA) + " plus 1: \n" + Arrays.toString(plusOne(digitsA)));
    System.out.println("digitsB " + Arrays.toString(digitsB) + " plus 1: \n" + Arrays.toString(plusOne(digitsB)));
  }
}
