package Algorithms.Hackerrank;
import java.util.*;

/**
 * Given two strings, first and second, that may or may not be of the same length, determine the minimum number of character deletions required to make them anagrams.
 * Any characters can be deleted from either of the strings.
 *
 * Created by dianaluca on 11/15/16.
 */

public class MakingAnagrams {
  public static int numberNeeded(String first, String second) {
    HashMap<Character, Integer> hmFirst = new HashMap<Character, Integer>();
    HashMap<Character, Integer> hmSecond = new HashMap<Character, Integer>();
    int n = first.length();
    int m = second.length();
    int res = 0;

    for(int i = 0; i < n; i++) {
      int val = hmFirst.get(first.charAt(i)) == null ? 0 : hmFirst.get(first.charAt(i));
      hmFirst.put(first.charAt(i), val+1);
    }
    for(int i = 0; i < m; i++) {
      int val = hmSecond.get(second.charAt(i)) == null ? 0 : hmSecond.get(second.charAt(i));
      hmSecond.put(second.charAt(i), val+1);
    }

    //calculate response res
    for (Character key : hmFirst.keySet()) {
      if (hmSecond.containsKey(key)) //common elements: found in both strings
        res += Math.abs(hmFirst.get(key) - hmSecond.get(key));
      else res += hmFirst.get(key); //characters found only in the "first" string
    }
    for (Character key : hmSecond.keySet()) {
      if (!hmFirst.containsKey(key)) //characters found only in the "second" string
        res += hmSecond.get(key);
    }

    return res;
  }

  /**
   * Test Case:
   *
   * Sample Input
   * cde
   * abc
   *
   * Sample Output
   * 4
   */

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String a = in.next(); //cde
    String b = in.next(); //abc
    System.out.println(numberNeeded(a, b)); //4
  }


}
