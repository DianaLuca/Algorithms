package LeetCodeAlgorithms;

/**
 * Given a non-empty integer array of size n,
 * find the minimum number of moves required to make all array elements equal,
 * where a move is incrementing n - 1 elements by 1.
 *
 *
 * Incrementing all but one is equivalent to decrementing that one.
 * How many single-element decrements to make all equal?
 * Just take the difference from what's currently there (the sum) to what we want (n times the minimum).
 *
 * Created by dianaluca on 11/9/16.
 */

public class MinimumMovesToEqualArrayElements453 {
  public static int minMoves(int[] nums) {
    int N = nums.length;
    int min = Integer.MAX_VALUE;
    int sum = 0;

    for (int i = 0; i < N; i++) {
      min = Math.min(min, nums[i]);
      sum += nums[i];
    }

    return sum - (min * N);
  }

  /**
   * Example:
   * Input: [1,2,3]
   * Output: 3
   * Explanation:
   * Only three moves are needed (remember each move increments two elements):
   * [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
   * @param args
   */

  public static void main(String[] args) {
    int[] nums = {1, 2, 3};
    System.out.println("Minimum number of moves is: " + minMoves(nums));
  }
}
