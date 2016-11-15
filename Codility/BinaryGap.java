package Algorithms.Codility;

import java.util.ArrayList;

/**
 * Find longest sequence of zeros in binary representation of an integer.
 *
 * https://codility.com/programmers/lessons/1-iterations/
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
}
