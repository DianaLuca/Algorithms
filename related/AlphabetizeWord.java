package Algorithms.related;

import java.util.Arrays;

/**
 * Reorder the word's letters into alphabetical order. Return the result
 *
 * Created by dianaluca on 11/4/16.
 */

public class AlphabetizeWord {
  public static String alphabetize(String word) {
    char[] W = word.toCharArray();
    Arrays.sort(W);
    return new String(W);
  }

  public static void main(String[] args) {
    String word = "bcdaba";
    String res = alphabetize(word);
    System.out.println(res);
  }
}
