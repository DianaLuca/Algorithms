package LeetCodeAlgorithms.related;

import java.util.Arrays;

/**
 * Find longest series of ones in a binary digit array
 *
 * Created by dianaluca on 11/12/16.
 */
public class BinaryOnesSequence {
  public static int solution(int N) {
      String bits = Integer.toBinaryString(N);
      System.out.println("bits = " + bits);

      String[] split = bits.split("0+");
      System.out.println("After splitting bits after 0+ " + Arrays.toString(split));

      if(split.length == 0) return 0;
      Arrays.sort(split);
      int maxLength = split[split.length - 1].length();
      return maxLength;
  }

  public static void main(String[] args) {
    int res = solution(2147483640);
    System.out.println("Longest series of ones has the length =  " + res);
  }
}
