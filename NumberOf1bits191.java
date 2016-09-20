package LeetCode;

/**
 * Created by dianaluca on 9/19/16.
 */
public class NumberOf1bits191 {
  public static int hammingWeight(int n) {
    String nrString = Integer.toBinaryString(n);
    int cnt = 0;
    for (int i = 0; i < nrString.length(); i++){
      if (nrString.charAt(i) == '1') cnt++;
    }
    return cnt;
  }

  public static int hammingWeightMask(int n) {
    int bits = 0;
    int mask = 1;    // 00000...01 (32 bits)
    System.out.println(mask);
    for (int i = 0; i < 32; i++) {
      if ((n & mask) != 0) {
        bits++;
      }
      mask <<= 1;
      System.out.println(mask);
    }
    return bits;
  }

  public static int hammingWeightDiffTrick (int n) {
    int sum = 0;
    while (n != 0) {
      sum++;
      n &= n - 1;
    }
    return sum;
  }

  public static void main(String[] args){
    System.out.println("1'st method: with Integer.toBinaryString() method: ");
    System.out.println(hammingWeight(1));
    System.out.println("2'nd method: with shifting mask with 1 bit: ");
    System.out.println(hammingWeightMask(15));
    System.out.println("3'nd method: using trick to make AND on predecessor and itself: ");
  }
}
