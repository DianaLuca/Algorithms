package LeetCodeAlgorithms;

/**
 * You are climbing a stair case. It takes n steps to reach to the top.
 * Each time you can either climb 1 or 2 steps.
 * In how many distinct ways can you climb to the top?
 *
 * obs: Fibonacci Numbers : 1, 2, 3, 5, 8, 13, 21, 34 etc
 * (where Fibonacci nrs represents the nr #ways to climb for each nr of stairs)
 *
 * Created by dianaluca on 9/19/16.
 */

public class ClimbingStairs70 {
  public static int climbStairs(int n) {
    if (n == 0) return n;
    int a = 0;
    int b = 1;
    int cnt = 0;
    for(int i = 1; i <= n; i++){
      cnt = a + b;    //i1: cnt=1    i2: cnt=2  i3: cnt=3    i4: cnt=5   i5: cnt=8   i6: cnt=13
      a = b;          //i1: a=1      i2: a=1    i3: a=2      i4: a=3     i5: a=5     i6: a=8
      b = cnt;        //i1: b=1      i2: b=2    i3: b=3      i4: b=5     i5: b=8     i6: b=13
    }
    return cnt;
  }

  public static void main(String[] args) {
    int N = 6;
    for(int i = 0; i <= N; i++){
      System.out.println(i + " stairs in " + climbStairs(i) + " ways.");
      //should return 0, 1, 2, 3, 5, 8, 13
    }
  }
}
