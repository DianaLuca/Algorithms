package Algorithms.CSAcademy;

import java.util.Scanner;

/**
 * You are given a list of NN words. From each word you should keep only one letter and discard all the others.
 * Then you should permute the NN chosen letters and build a single word by concatenating them.
 * Find the lexicographically smallest word you can obtain.
 *
 * https://csacademy.com/contest/interview-archive/#task/one_letter/
 *
 * Created by dianaluca on 11/12/16.
 */

public class OneLetter {
  public static void main (String[] args) throws Exception {
    // Starting coding here
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    StringBuilder res = new StringBuilder();

    for (int i = 0; i < N; i++) {
      String word = sc.next();
      int len = word.length();
      int min = Integer.MAX_VALUE;
      int index = 0;

      for (int j = 0; j < len; j++) {
        char c = word.charAt(j);
        int x = c - 'a';
        if (min > x) {
          min = x;
          index = j;
        }
      }
      res.append(word.charAt(index));
    }

    String result = res.toString();
    res = new StringBuilder();
    int[] alphabet = new int[26];
    for (int i = 0; i < N; i++) {
      char c = result.charAt(i);
      int x = c - 'a';
      alphabet[x]++;
    }
    for (int i = 0; i < 26; i++) {
      int val = alphabet[i];
      if (val == 0) continue;

      int chVal = i + 97;
      char c = (char) chVal;
      while(val-- > 0) {
        res.append(c);
      }
    }

    System.out.println(res.toString());
  }
}
