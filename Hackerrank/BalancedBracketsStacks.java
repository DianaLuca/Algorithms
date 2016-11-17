package Algorithms.Hackerrank;
import java.util.*;

/**
 * A bracket is considered to be any one of the following characters: (, ), {, }, [, or ]
 *
 * Given n strings of brackets, determine whether each sequence of brackets is balanced.
 * If a string is balanced, print YES on a new line; otherwise, print NO on a new line.
 *
 * Created by dianaluca on 11/17/16.
 */

public class BalancedBracketsStacks {
  public static boolean isBalanced(String expression) {
    int N = expression.length();
    Stack<Character> stack = new Stack<>();
    char bracket = expression.charAt(0);

    for (int i = 0; i < N; i++) {
      bracket = expression.charAt(i);
      if (bracket == '(' || bracket == '[' || bracket == '{') stack.push(bracket);
      else if(bracket == ')' && !stack.isEmpty() && stack.peek() == '(') stack.pop();
      else if(bracket == ']' && !stack.isEmpty() && stack.peek() == '[') stack.pop();
      else if(bracket == '}' && !stack.isEmpty() && stack.peek() == '{') stack.pop();
      else return false;
    }

    return stack.isEmpty();
  }

  /**
   * Sample Input
   * 3
   * {[()]}
   * {[(])}
   * {{[[(())]]}}
   *
   * Sample Output
   * YES
   * NO
   * YES
   */

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    for (int i = 0; i < n; i++) {
      String expression = sc.next();
      System.out.println( (isBalanced(expression)) ? "YES" : "NO" );
    }
  }

}
