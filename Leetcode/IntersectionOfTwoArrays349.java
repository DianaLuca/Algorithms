package Algorithms.Leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Set;

/**
 * Given two arrays, write a function to compute their intersection.

 * Example:
 * Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
 * Note:
 * Each element in the result must be unique.
 * The result can be in any order.
 *
 * Created by dianaluca on 9/14/16.
 */

public class IntersectionOfTwoArrays349 {
  public static int[] intersection(int[] nums1, int[] nums2) {
    HashMap hm1 = hashMp(nums1);
    HashMap hm2 = hashMp(nums2);

    ArrayList<Integer> res = new ArrayList<Integer>();
    Set<Integer> keys = hm1.keySet();

    for(int key : keys) {
      int val1 = (Integer)hm1.get(key);
      int val2 = hm2.get(key) == null ? 0 : (Integer)hm2.get(key);
      for(int i = 0; i < Math.min(val1, val2); i++) {
        res.add(key);
      }
    }

    int[] result = new int[res.size()];
    for (int i = 0; i < res.size(); i++) {
      result[i] = res.get(i);
    }
    return result;
  }

  public static HashMap hashMp(int[] arr) {
    HashMap hm = new HashMap<Integer, Integer>();
    for(int elem : arr) {
      int val = hm.get(elem) == null ? 0 : (Integer)hm.get(elem);
      hm.put(elem, ++val);
    }
    return hm;
  }

  public static void main(String[] args) {
    int[] a = {1, 2, 3, 2, 4};
    int[] b = {2, 2, 5};
    int[] c = intersection(a, b);
    System.out.println(Arrays.toString(c));
  }
}
