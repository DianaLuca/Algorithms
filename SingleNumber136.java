package LeetCode;

/**
 * Given an array of integers, every element appears twice except for one.
 * Find that single one.
 Note:
 * Your algorithm should have a linear runtime complexity.
 * Could you implement it without using extra memory?
 * Created by dianaluca on 9/15/16.
 */

public class SingleNumber136 {
  public int singleNumber(int[] nums) {
    int N = nums.length;
    // HashMap <Integer, Integer> hm = new HashMap<Integer, Integer>();

    // int value = 1;
    // for (int i = 0; i < N; i++) {
    //     if (!hm.containsKey(nums[i])) hm.put(nums[i], 1);
    //     else hm.put(nums[i], hm.get(nums[i]) + 1);
    // }

    // for (Integer key: hm.keySet()) {
    //     if (hm.get(key) == 1) {
    //         return key;
    //     }
    // }

    int result = 0;
    for (int i = 0; i < N; ++i) {
      result ^= nums[i];
    }
    return result;
  }
}
