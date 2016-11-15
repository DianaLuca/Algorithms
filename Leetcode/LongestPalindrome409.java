package Algorithms.Leetcode;

import java.util.HashMap;
import java.util.Set;

/**
 * Given a string which consists of lowercase or uppercase letters,
 * find the length of the longest palindromes that can be built with those letters.
 * This is case sensitive, for example "Aa" is not considered a palindrome here.
 *
 * Input: "abccccdd"
 * Output: 7
 * Explanation:
 * One longest palindrome that can be built is "dccaccd", whose length is 7.
 *
 * Created by dianaluca on 10/3/16.
 */

public class LongestPalindrome409 {
  public static int longestPalindrome(String s) {
    if(s.length() == 1) return 1;
    if(s.length() == 2 && s.charAt(0) == s.charAt(1)) return 2;
    else if(s.length() == 2 && s.charAt(0) != s.charAt(1)) return 1;

    HashMap<Character, Integer> hm = new HashMap<>();
    for(int i = 0; i < s.length(); i++ ) {
      int val = hm.get(s.charAt(i)) == null ? 0 : (Integer) hm.get(s.charAt(i));
      hm.put(s.charAt(i), ++val);
    }

    int palSize = 0;
    boolean odd = false;
    Set<Character> keys = hm.keySet();
    for(Character key : keys) {
      int val = hm.get(key);
      if (val % 2 == 0)   palSize += val;
      else {
        palSize += (val-1);
        odd = true;
      }
    }

    if(odd) return palSize + 1;
    else return palSize;
  }

  public static void main(String[] args) {
    String s = "abccccdd";
    int pl = longestPalindrome(s);
    System.out.println(pl);
  }
}
