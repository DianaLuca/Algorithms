package Algorithms.Leetcode;

/**
 * Created by dianaluca on 10/31/16.
 */
public class LongestSubstringWithoutRepeatingCharacters3 {
  public static int getNumericValue (String s, int pos) {
    return s.charAt(pos);
  }

  public static int lengthOfLongestSubstring(String s) {
    if (s.length() == 0)
      return 0;

    int[] freq = new int[256];

    int left = 0;
    int right = 0;
    int result = 0;

    freq[getNumericValue(s, 0)]++;

    int N = s.length();

    for (left = 0; left < N; left++) {
      while (right + 1 < N && freq[getNumericValue(s, right + 1)] == 0) {
        freq[getNumericValue(s, right + 1)]++;
        ++right;
      }
      result = Math.max(result, right - left + 1);

      freq[getNumericValue(s, left)]--;
    }

    return result;
  }

  public static void main(String[] args) {
    String s = "dvdf"; //3
    System.out.println(lengthOfLongestSubstring(s));
  }
}
