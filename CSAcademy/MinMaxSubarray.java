package Algorithms.CSAcademy;

import java.util.Scanner;

/**
 * You are given an array of size NN. The elements of the array are not necessarily distinct.
 * Find the shortest subarray that contains at least one of the minimum and one of the maximum values.
 *
 * Desired solution
 * You should solve this problem in O(N).
 *
 * https://csacademy.com/contest/interview-archive/#task/min-max-subarray/
 *
 * Created by dianaluca on 11/12/16.
 */

public class MinMaxSubarray {
  public static void main (String[] args) throws Exception {
    // Starting coding here
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int[] arr = new int[N];
    int max = Integer.MIN_VALUE;
    int min = Integer.MAX_VALUE;
    int imax, imin;
    imin = imax = 0;
    int delta = N;

    int i = 0;
    while (i < N && sc.hasNext()) {
      arr[i] = sc.nextInt();
      if (max < arr[i]) {
        max = arr[i];
        imax = i;
      }
      if (min > arr[i]) {
        min = arr[i];
        imin = i;
      }
      i++;
    }

    for (int j = 0; j < N; j++) {
      if (min == arr[j]) imin = j;
      if (max == arr[j]) imax = j;
      delta = Math.min(Math.abs(imin - imax) + 1, delta);
    }

    System.out.println(delta);
  }
}
