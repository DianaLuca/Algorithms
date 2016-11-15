package Algorithms.related;
import java.util.*;

/**
 * Find longest sequence of zeros in binary representation of an integer.
 *
 * Created by dianaluca on 11/12/16.
 */

public class BinaryGap {
  public static int solution(int N) {
    if (N == 0) return 0;
    int res = Integer.MIN_VALUE;
    ArrayList<Integer> arr = new ArrayList<>();

    while (N > 0) {
      long twosPow = 1;
      int pow = 1;
      while (twosPow <= N && twosPow <= 1<<30) {
        twosPow *= 2;
        pow++;
      }

      if (twosPow == N) arr.add(pow);
      else {
        twosPow /= 2;
        pow--;
        arr.add(pow);
      }
      N = N - (int)twosPow;
    }

    if (arr.size() == 1) return 0;
    for (int i = 1; i < arr.size(); i++) {
      res = Math.max(res, arr.get(i-1)-arr.get(i) - 1);
    }

    return res;
  }

  public static void main(String[] args) {
    //int res = solution(529); //4
    //int res = solution(15); //0
    //int res = solution(9); //2
    //int res = solution(1041); //5
    //int res = solution(1376796946);
    //System.out.println(Integer.toBinaryString(1376796946));
    int res = solution(2147483647);

    // 2147483647
    // 1376796946
    System.out.print(res);
  }
}
