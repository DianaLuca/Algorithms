package LeetCodeAlgorithms;

import java.util.Arrays;
import java.util.HashMap;

/**
 * Given an array of integers, return indices of the two numbers such that they add up to a specific target.
 * You may assume that each input would have ""exactly one"" solution.
 *
 * Created by dianaluca on 11/2/16.
 */

public class TwoSum1 {

  /**
   * Solution 1: time O(N) space O(N)
   */
  public static int[] twoSum(int[] nums, int target) {
    int N = nums.length;
    HashMap<Integer, Integer> hm = new HashMap<>(N);

    for (int i = 0; i < N; i++) {
      // hm(key: nums values; val: corresponding nums indexes)
      if (hm.containsKey( target - nums[i])) return new int[] {i, hm.get(target - nums[i])};
      else    hm.put(nums[i], i);
    }

    return null;
  }

  /**
   * Solution 2: time O(N^2) in-place
   */
  public static int[] twoSumNN(int[] nums, int target) {
    int N = nums.length;

    for (int i = 0; i < N; i++) {
      int j = N-1;
      while (j > i) {
        if (nums[i] + nums[j] == target)
          return new int[] {i, j};
        --j;
      }
    }
    return null;
  }

  public static void main(String[] args) {
    int[] arr = {1,2,3,5,9,4,7};
    System.out.println(Arrays.toString(twoSum(arr, 11)));
  }
}
