package Algorithms.CSAcademy;

import java.util.Arrays;
import java.util.Scanner;

/**
 * You are given two arrays of integers. You should find all their common elements.
 * The arrays do not necessarily contain distinct values.
 * If a certain integer appears in the first array x times and in the second array y times,
 * the output should contain it exactly min(x,y) times.
 *
 * Desired solution
 * You should solve this problem in O(N_1 + N_2)
 *
 * Also try solving it using only O(1) additional memory. What's the best complexity you can find?
 *
 * https://csacademy.com/contest/interview-archive/#task/array-intersection/
 *
 * Created by dianaluca on 11/12/16.
 */

public class ArrayIntersection {

  public static void main (String[] args) throws Exception {
    // Starting coding here
    Scanner sc = new Scanner(System.in);
    int N1 = sc.nextInt();
    int N2 = sc.nextInt();
    int[] arr1 = new int[N1];
    int[] arr2 = new int[N2];

    for(int i = 0; i < N1; i++) {
      arr1[i] = sc.nextInt();
    }

    for(int i = 0; i < N2; i++) {
      arr2[i] = sc.nextInt();
    }

    // Sort arrays O(N*logN) - quicksort
    Arrays.sort(arr1);
    Arrays.sort(arr2);

    int cnt = 0;
    int i = 0;
    int j = 0;
    StringBuilder res = new StringBuilder();

    // O(1) additional memory
    while (i < N1 && j < N2) {
      //System.out.println("arr1[i] = " +arr1[i] + ", arr2[j] = " + arr2[j]);
      if (arr1[i] == arr2[j]) {
        cnt++;
        res.append(arr1[i]).append(" ");
        i++;
        j++;
      } else if (arr1[i] < arr2[j]) {
        i++;
      } else {
        j++;
      }
    }

    System.out.println(cnt);
    System.out.println(res.toString());

  }
}
