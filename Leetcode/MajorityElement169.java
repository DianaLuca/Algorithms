package Algorithms.Leetcode;

import java.util.HashMap;
import java.util.Set;

/**
 * Given an array of size n, find the majority element.
 * The majority element is the element that appears more than ⌊ n/2 ⌋ times.
 * You may assume that the array is non-empty and
 * the majority element always exist in the array.
 *
 * Created by dianaluca on 9/15/16.
 */

public class MajorityElement169 {
  public int majorityElement(int[] nums) {
    int N = nums.length;
    HashMap hm = new HashMap<Integer, Integer>();
    for(int i = 0; i < nums.length; i++){
      int val = hm.get(nums[i]) == null ? 0 : (Integer) hm.get(nums[i]);
      hm.put(nums[i], ++val);
    }

    Set<Integer> keys = hm.keySet();
    for(Integer key : keys){
      int val = (Integer)hm.get(key);
      if(val > N/2){
        return key;
      }
    }
    return -1;
  }
}
