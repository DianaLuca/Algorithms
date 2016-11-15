package Algorithms.CSAcademy;

import java.util.Scanner;

/**
 * On a field represented as a matrix of N rows and M columns there is a donkey and two haystacks.
 * The donkey is really hungry and he wants to get to a haystack as fast as possible.
 * He can walk in four directions: up, down, left or right.
 * The paradox of the donkey is that if the two haystacks are equally close to him
 * he won't be able to decide which one to choose and he will starve to death.
 * You are given the cells of the haystackes, but you don't know where the donkey is.
 * Compute the number of cells where the donkey will starve if he's there.
 *
 * https://csacademy.com/contest/interview-archive/#task/donkey-paradox/
 *
 * Created by dianaluca on 11/12/16.
 */

public class DonkeyParadox {
  public static void main (String[] args) throws Exception {
    // Starting coding here
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int M = sc.nextInt();
    int hayx1 = sc.nextInt() -1;
    int hayy1 = sc.nextInt() -1;
    int hayx2 = sc.nextInt() -1;
    int hayy2 = sc.nextInt() -1;
    int cnt = 0;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        int delta1 = Math.abs(i-hayx1) + Math.abs(j-hayy1);
        int delta2 = Math.abs(i-hayx2) + Math.abs(j-hayy2);
        if (delta1 == delta2)
          cnt++;
      }
    }
    System.out.println(cnt);
  }
}
