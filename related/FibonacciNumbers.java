package Algorithms.related;

/**
 * The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
 * The next number is found by adding up the two numbers before it.
 *
 * N - calculate fibonacci for N numbers
 *
 * Created by dianaluca on 10/4/16.
 */

public class FibonacciNumbers {
  public static int fibonacci(int N) {
    if (N == 0) return 0;

    int varA = 0;
    int varB = 1;
    int next;

    for(int i = 2; i < N; i++) {
      next = varA + varB;
      varA = varB;
      varB = next;
    }

    return (varA + varB);

  }

  public static void main (String[] args) {
    int res = fibonacci(7); //return 13
    System.out.println(res);
  }
}
