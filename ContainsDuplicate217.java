package LeetCode;

import java.util.HashMap;

/**
 * Given an array of integers, find if the array contains any duplicates.
 * Your function should return true if any value appears at least twice in the array,
 * and it should return false if every element is distinct.
 *
 * Created by dianaluca on 9/15/16.
 */

public class ContainsDuplicate217 {
  public boolean containsDuplicate(int[] nums) {
    int N = nums.length;
    if (N == 0) return false;

    HashMap hs = new HashMap<Integer, Integer>();

    for(int i = 0; i< N; i++){
      int val = hs.get(nums[i]) == null ? 0 : (Integer) hs.get(nums[i]);
      hs.put(nums[i], ++val);
      if (val >= 2) return true;
    }

    return false;
  }
}
