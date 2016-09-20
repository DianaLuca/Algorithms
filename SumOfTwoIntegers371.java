package LeetCode;

/**
 * Calculate the sum of two integers a and b,
 * but you are not allowed to use the operator + and -.
 *
 * Created by dianaluca on 9/15/16.
 */

public class SumOfTwoIntegers371 {
  public int getSum(int a, int b) {

    // Solution1: --------------------------

    //     while (b != 0) {
    //         int carry = a & b; // and
    //         a = a ^ b; // xor
    //         b = carry << 1; //left shift
    //     }
    //     return a;

    // Solution 2: ---------------------------

    int result = 0;
    int pow = 1;
    int carry = 0;
    int val = 0;

    while ((a > 0) || (b > 0) || (carry>0)) {
      val = carry ^ (a&1) ^ (b&1);

      if (carry > 0) {
        carry = (a&1) | (b&1);
      } else {
        carry = a & b & 1;
      }

      result |= (pow * val);

      a >>= 1;
      b >>= 1;
      pow <<= 1;
    }

    return result;

  }
}
