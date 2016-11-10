package LeetCodeAlgorithms;

import java.util.ArrayList;
import java.util.List;

/**
 * Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
 * Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
 * The order of output does not matter.
 *
 * Created by dianaluca on 11/10/16.
 */

public class FindAllAnagramsInaString438 {
  public static int hash(String word) {
    int len = word.length();
    int sum = 0;
    int xor = 0;
    int sqSum = 0;

    for(int i = 0; i < len; i++) {
      int val = Character.getNumericValue(word.charAt(i));
      sum += val;
      xor ^= val;
      sqSum += val * val;
    }

    return sum * 11 + xor * 11 + sqSum * 2;
  }

  public static List<Integer> findAnagrams(String s, String p) {
    List<Integer> res = new ArrayList<>();
    int N = s.length();
    int M = p.length();
    int hashS = hash(s);
    int hashP = hash(p);

    if ( N <= M && hashS == hashP)
      res.add(0);

    for(int i = 0; i <= N-M; i++) {
      int j = i + M;
      String tmpStr = s.substring(i, j);
      hashS = hash(tmpStr);

      if (hashP == hashS) res.add(i);
    }

    return res;
  }

  /**
   * Input:
   s: "abab" p: "ab"

   Output:
   [0, 1, 2]

   Explanation:
   The substring with start index = 0 is "ab", which is an anagram of "ab".
   The substring with start index = 1 is "ba", which is an anagram of "ab".
   The substring with start index = 2 is "ab", which is an anagram of "ab".
   */

  public static void main(String[] args) {
    String s = "abab";
    String p = "ab";
    System.out.println(findAnagrams(s, p));
  }
}
