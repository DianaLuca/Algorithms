package Algorithms.Hackerrank;
import java.util.*;

/**
 * Davis has s staircases in his house and he likes to climb each staircase 1, 2, or 3 steps at a time.
 * Being a very precocious child, he wonders how many ways there are to reach the top of the staircase.
 * Given the respective heights for each of the s staircases in his house,
 * find and print the number of ways he can climb each staircase on a new line.


 * Created by dianaluca on 11/19/16.
 */
public class DavisStaircaseRecursion {
  /**
   * For each staircase, print the number of ways Davis can climb it in a new line.

   Sample Input

   3    - s = 3 - number of stairs
   1    - print for stair 1 the number of ways he can climb each staircase on a line
   3    - print for stair 3 the number of ways he can climb each staircase on a line
   7    - print for stair 7 the number of ways he can climb each staircase on a line

   Sample Output

   1
   4
   44

   */
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int s = in.nextInt();
    for(int a0 = 0; a0 < s; a0++){
      int n = in.nextInt();
      System.out.println(waysClimbingN(n));
    }
  }

  public static int waysClimbingN(int n) {
    if(n == 1) return 1;
    else if(n == 2) return 2;
    else if(n == 3) return 4;
    //else return (waysClimbingN(n-1) + waysClimbingN(n-2) + waysClimbingN(n-3));

    int a = 1, b = 2, c = 4;
    int i = 4, sum = 0;
    while(i<=n){
      sum = a + b + c;
      a = b;
      b = c;
      c = sum;
      i++;
    }
    return sum;
  }
}
