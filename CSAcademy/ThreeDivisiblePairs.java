package Algorithms.CSAcademy;

import java.util.Scanner;

/**
 * You are given an array of N positive integers.
 * Compute the number of pairs of integers in the array that have the sum divisible by 3.
 *
 * https://csacademy.com/contest/interview-archive/#task/3-divisible-pairs/
 *
 * Created by dianaluca on 11/12/16.
 */

public class ThreeDivisiblePairs {
  public static void main (String[] args) throws Exception {
    // Starting coding here
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    long[] freq = new long[3];

    for (int i = 0; i < N; i++) {
      int crr = sc.nextInt();
      freq[crr % 3]++;
    }

    long res = (freq[0] * (freq[0] - 1))/2 + freq[1]*freq[2];
    System.out.println(res);

  }
}
