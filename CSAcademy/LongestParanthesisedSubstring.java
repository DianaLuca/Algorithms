package Algorithms.CSAcademy;

import java.util.Scanner;
import java.util.Stack;

/**
 * You are given a string SS consisting only of parentheses.
 * Compute the size of the longest substring which is correctly parenthesised.
 *
 * Desired solution
 * Try solving the problem in O(len(S)).
 *
 * https://csacademy.com/contest/interview-archive/#task/longest-parenthesised-substring/
 *
 * Created by dianaluca on 11/12/16.
 */

public class LongestParanthesisedSubstring {
  public static void main (String[] args) throws Exception {
    // Starting coding here

    Stack<Integer> leftIndex = new Stack<>();
    Scanner sc = new Scanner(System.in);
    String s = sc.next();
    int N = s.length();
    int start = -1;
    int res = -1;

    for (int i = 0; i < N; i++) {
      char ch = s.charAt(i);
      if (ch == '(') {
        leftIndex.push(i);
      } else {   // ch == ')'
        if (leftIndex.empty()) {
          start = i;
        } else {
          leftIndex.pop();
          if (leftIndex.empty()) {
            res = Math.max(res, i - start);
          } else {
            res = Math.max(res, i - leftIndex.peek());
          }
        }
      }
    }
    System.out.println(res);
  }
}
