package Algorithms.Hackerrank;
import java.util.*;

/**
 * Created by dianaluca on 11/19/16.
 */
public class FibonacciNumbersRecursion {
  public static int fibonacci(int n) {
    // Complete the function.
    if (n == 0) return 0;
    int a = 0;
    int b = 1;
    int res = 0;

    for(int i = 2; i <= n; i++) {
      res = a + b;
      a = b;
      b = res;
    }

    return res;
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    scanner.close();
    System.out.println(fibonacci(n));
  }
}
