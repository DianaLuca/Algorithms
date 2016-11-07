package LeetCodeAlgorithms;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
 * Find all unique quadruplets in the array which gives the sum of target.
 * Note: The solution set must not contain duplicate quadruplets.
 *
 * Created by dianaluca on 11/7/16.
 */

public class FourSum18 {
  public static List<List<Integer>> fourSum(int[] nums, int target) {
    List<List<Integer>> res = new ArrayList<>();
    int N = nums.length;
    if (N < 4 ) return res;
    Arrays.sort(nums);

    int ii = 0;
    while (ii < N-3) {
      if (nums[ii] > target && target >= 0) break;
      int i = ii+1;
      while ( i < N-2) {
        int j = i+1;
        int k = N-1;

        while (j < k) {
          int sum = nums[ii] + nums[i] + nums[j] + nums[k];
          if (sum == target) res.add(Arrays.asList(nums[ii], nums[i], nums[j], nums[k]));
          if (sum <= target) while (nums[j++] == nums[j] && j < k);
          if (sum >= target) while (nums[k--] == nums[k] && j < k);
        }
        while (nums[i] == nums[++i] && i < N-2);
      }
      while (nums[ii] == nums[++ii] && ii < N-2);
    }

    return res;
  }

  /**
   * For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
   * A solution set is:
   * [
   *  [-1,  0, 0, 1],
   *  [-2, -1, 1, 2],
   *  [-2,  0, 0, 2]
   *   ]
   */
  public static void main(String[] args) {
    int[] S = {1, 0, -1, 0, -2, 2};
    int target = 0;
    System.out.println(fourSum(S, target));
  }
}
