package Algorithms.Leetcode;

/**
 * You are a professional robber planning to rob houses along a street.
 * Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is
 * that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
 * Given a list of non-negative integers representing the amount of money of each house,
 * determine the maximum amount of money you can rob tonight without alerting the police.
 *
 * Created by dianaluca on 9/27/16.
 */
public class HouseRobber198 {

  public int rob(int[] nums) {
    int N = nums.length;
    if (N == 0) return 0;

    // ------------ 1'st method: --------------
    int[] ROB = new int[N];
    int[] FREE = new int[N];

    FREE[0] = 0;
    ROB[0] = nums[0];

    for (int i = 1; i < N; ++i) {
      ROB[i] = nums[i] + FREE[i-1];
      FREE[i] = 0 + Math.max(ROB[i-1], FREE[i-1]);
    }
    return Math.max(ROB[N-1], FREE[N-1]);


    // -------------- 2'nd method: ----------------
    // if (N == 1) return nums[0];

    // int[] ROB = new int[N];

    // ROB[0] = nums[0];
    // int best_result = ROB[0];

    // for (int i = 1; i < N; ++i) {
    //     int prev2 = (i >= 2 ? ROB[i-2] : 0);
    //     int prev3 = (i >= 3 ? ROB[i-3] : 0);
    //     ROB[i] = nums[i] + Math.max(prev2, prev3);

    //     best_result = Math.max(ROB[i], best_result);
    // }
    // return best_result;

  }

}
