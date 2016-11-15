package Algorithms.Leetcode;

/**
 * Created by dianaluca on 10/11/16.
 */

public class ConvertaNumbertoHexadecimal405 {
  public static String toHex(int num) {
    if (num == 0) return "0";

    StringBuilder res = new StringBuilder();
    char[] he = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};

    long lgn = num;
    if (lgn < 0)
      lgn = (1L << 32) + lgn;

    while (lgn != 0) {
      res.append (he[(int)(lgn % 16)]);
      lgn /= 16;
    }

    return res.reverse().toString();
  }

  public static void main(String[] args) {
    String hexadeci = toHex(260);
    System.out.println(hexadeci);  // print "104"
  }
}
