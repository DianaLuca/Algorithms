package LeetCode;

import java.util.HashSet;

/**
 * Write an algorithm to determine if a number is "happy".
 A happy number is a number defined by the following process:
 Starting with any positive integer, replace the number by the sum of the squares of its digits,
 and repeat the process until the number equals 1 (where it will stay),
 or it loops endlessly in a cycle which does not include 1.
 Those numbers for which this process ends in 1 are happy numbers.
 Example: 19 is a happy number
 12 + 92 = 82
 82 + 22 = 68
 62 + 82 = 100
 12 + 02 + 02 = 1
 **
 * Created by dianaluca on 9/19/16.
 */

public class HappyNumber202 {
  HashSet hm = new HashSet<Integer>();

  public boolean isHappy(int n) {
    if (n == 0) return false;
    if (n == 1) return true;

    if (hm.contains (n))
      return false;
    hm.add(n);

    // int val = hm.get(n) == null ? 0 : (Integer)hm.get(n);
    // if(val != 0) return false;
    // hm.put(n, ++val);

    int res = 0;
    while(n > 0) {
      int tmp = 0;
      tmp = n % 10;
      res += tmp * tmp;
      n /= 10;
    }

    return isHappy(res);
  }

}
