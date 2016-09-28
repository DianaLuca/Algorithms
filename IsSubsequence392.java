package LeetCodeAlgorithms;

import java.util.Scanner;

/**
 * Example 1:
 * s = "abc", t = "ahbgdc"
 * Return true.
 *
 * Example 2:
 * s = "axc", t = "ahbgdc"
 * Return false.
 *
 * Follow up:
 * If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B,
 * and you want to check one by one to see if T has its subsequence.
 * In this scenario, how would you change your code?
 *
 * Created by dianaluca on 9/28/16.
 */

public class IsSubsequence392 {
  public static boolean isSubsequence(String s, String t) {
    int N = s.length();
    int M = t.length();

    if (N == 0) return true;
    if (M == 0) return false;

    int i = 0;
    int j = 0;
    while (j < M && i < N) {
      if (s.charAt(i) == t.charAt(j)) {
        i++;
        j++;
      }  else j++;
    }

    if (i < N) return false;
    else return true;
  }

  // test client
  public static void main(String[] args) {
    Scanner sc =  new Scanner(System.in);
    String s = sc.nextLine();
    String t = sc.nextLine();

    //int[][] table = nextInTable(t);
    //printTable(table);

    boolean toBeOrNotSubseq = isSubsequence(s, t);
    System.out.println(toBeOrNotSubseq);
  }
}
