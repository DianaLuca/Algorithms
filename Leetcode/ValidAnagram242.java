package Algorithms.Leetcode;

import java.util.HashMap;

/**
 * Given two strings s and t,
 * write a function to determine if t is an anagram of s.
 * For example,
 * s = "anagram", t = "nagaram", return true
 * s = "rat", t = "car", return false.
 *
 * Note:
 * You may assume the string contains only lowercase alphabets.
 *
 * Follow up:
 * What if the inputs contain unicode characters?
 * How would you adapt your solution to such case?
 *
 * Created by dianaluca on 9/15/16.
 */

public class ValidAnagram242 {
  public boolean isAnagram(String s, String t) {
    HashMap smap = hashMp(s);
    HashMap tmap = hashMp(t);
    return smap.equals(tmap);
  }

  public HashMap<Character, Integer> hashMp(String s) {
    HashMap hm = new HashMap<Character, Integer>();
    for (char c : s.toCharArray()) {
      int val = hm.get(c) == null ? 0 : (Integer)hm.get(c);
      hm.put(c, ++val);
    }
    return hm;
  }
}
