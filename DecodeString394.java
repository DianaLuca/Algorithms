package LeetCodeAlgorithms;

import java.util.Stack;

/**
 * Given an encoded string, return it's decoded string
 * The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
 * Note that k is guaranteed to be a positive integer.
 * You may assume that the input string is always valid;
 * No extra white spaces, square brackets are well-formed, etc.
 * Furthermore, you may assume that the original data does not contain any digits
 * and that digits are only for those repeat numbers, k.
 * For example, there won't be input like 3a or 2[4].
 *
 * Examples:
 *
 * s = "3[a]2[bc]", return "aaabcbc".
 * s = "3[a2[c]]", return "accaccacc".
 * s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
 *
 * Created by dianaluca on 10/19/16.
 */

public class DecodeString394 {
  public static String decodeString(String s) {
    StringBuilder res = new StringBuilder();
    Stack<Integer> stackDigit = new Stack<>();
    Stack<Integer> stackIndex = new Stack<>();
    int cnt = 0;

    for (int i = 0; i < s.length(); i++) {
      char c = s.charAt(i);
      boolean isDigit = (c >= '0' && c <= '9');

      if (isDigit) {
        cnt = cnt*10 + c - '0';
        continue;

      } else if (c == '[') {
        stackDigit.push(cnt);
        stackIndex.push(res.length());
        cnt = 0;
        continue;

      } else if (c == ']') {
        StringBuilder tmpSb = new StringBuilder();
        int repeat = stackDigit.pop();
        int index = stackIndex.pop();
        while (--repeat > 0) {
          tmpSb.append(res.toString().substring(index));
        }
        res.append(tmpSb.toString());
        continue;
      }
      res.append(c);
    }

    return res.toString();
  }

  public static void main(String[] args) {
    String s1 = "3[a]2[bc]d";
    String s2 = "23[ab]";
    String decoded1 = decodeString(s1);  //print: "aaabcbcd"
    String decoded2 = decodeString(s2);
    System.out.println(decoded1);
    System.out.println(decoded2);
  }
}
