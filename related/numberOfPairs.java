package LeetCodeAlgorithms.related;

import java.util.HashMap;

/**
 * Return the number of pairs which summed are equal to sum
 *
 * Created by dianaluca on 11/1/16.
 */

public class numberOfPairs {

  /**
   * Solution 1: time O(N), space O(N), working for unordered arrays
   * @param arr
   * @param sum
   * @return
   */
  public static int numberOfPairs(int[] arr, int sum) {
    int res = 0;
    int N = arr.length;
    HashMap<Integer, Integer> hm = new HashMap<>(N);

    for (int i = 0; i < N; i++) {
      int key = sum - arr[i];
      int val = hm.get(arr[i]) == null ? 0 : hm.get(arr[i]);
      if (hm.containsKey(key)) res += hm.get(key);
      else hm.put(arr[i], val + 1);
    }
    return res;
  }

  /** TO DO:
   * Solution 2: in-place (with 2 pointers) for ordered arrays
   * @param args
   */

  public static void main(String[] args) {
    int[] arr = {0, 1, 2, 7, 12, 5, 6, 3, 8, 9, 10, 11, 9};

    System.out.println(numberOfPairs(arr, 11));
  }
}
