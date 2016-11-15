package Algorithms.Leetcode;

import java.util.HashMap;

/**
 * Given a string, find the first non-repeating character in it and return it's index.
 * If it doesn't exist, return -1.
 *
 * Example:
 * s = "leetcode"
 * return 0.
 *
 * s = "loveleetcode",
 * return 2.
 *
 * Created by dianaluca on 9/15/16.
 */

public class FirstUniqueCharacterInaString387 {
  public int firstUniqChar(String s) {
    int N = s.length();
    // LinkedHashMap hm = new LinkedHashMap<Character, Integer>();

    // for (int i = 0; i < N; i++){
    //     int val = hm.get(s.charAt(i)) == null ? 0 : (Integer) hm.get(s.charAt(i));
    //     hm.put(s.charAt(i), ++val);
    // }

    // Set<Character> keys = hm.keySet();
    // for (char key : keys) {
    //     System.out.println(key);
    //     if ((Integer)hm.get(key) == 1) {
    //         for (int i = 0; i < N; i++) {
    //             if (s.charAt(i) == key) return i;
    //         }
    //     }
    // }

    // Solution 2: ----------------------------------------

    HashMap hm = new HashMap< Character, Integer>();
    for (int i = 0; i < N; i++){
      int val = hm.get(s.charAt(i)) == null ? 0 : (Integer) hm.get(s.charAt(i));
      hm.put(s.charAt(i), ++val);
    }

    for (int i = 0; i < N; ++i) {
      if ((Integer)hm.get(s.charAt(i)) == 1) {
        return i;
      }
    }

    return -1;
  }
}
