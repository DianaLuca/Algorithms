package Algorithms.Leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
 * Find all unique triplets in the array which gives the sum of zero.
 * Note: The solution set must not contain duplicate triplets.
 *
 * Created by dianaluca on 11/3/16.
 */

public class Three3Sum15 {
  public static List<List<Integer>> threeSum(int[] nums) {
    List<List<Integer>> res = new ArrayList<>();
    int N = nums.length;
    if (N < 3 ) return res;
    Arrays.sort(nums);
    int i = 0;

    while (i < N-2) {
      if (nums[i] > 0) break;
      int j = i+1;
      int k = N-1;

      while (j < k) {
        int sum = nums[i] + nums[j] + nums[k];
        if (sum == 0) res.add(Arrays.asList(nums[i], nums[j], nums[k]));
        if (sum <= 0) while (nums[j++] == nums[j] && j < k);
        if (sum >= 0) while (nums[k--] == nums[k] && j < k);
      }
      while (nums[i++] == nums[i] && i < N-2);
    }

    return res;
  }

  /**
   * For example, given array S = [-1, 0, 1, 2, -1, -4],
   * A solution set is:
   * [
   *  [-1, 0, 1],
   *  [-1, -1, 2]
   * ]
   *
   * @param args
   */

  public static void main(String[] args) {
    int[] S = {-1, 0, 1, 2, -1, -4} ;
    List<List<Integer>> res = threeSum(S);
    System.out.println(res);
  }
}
