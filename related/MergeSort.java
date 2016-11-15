package Algorithms.related;

import java.util.Arrays;

/**
 * Merge Sort Algorithm: Top-down implementation using lists
 *
 * Created by dianaluca on 10/27/16.
 */

public class MergeSort {

  public static int[] mergeSort (int[] A) {
    int n = A.length;
    if (n <= 1) return A;
    int[] left = new int[n/2];
    int[] right = new int[n - n/2];

    for(int i = 0, j = 0, k = 0; i < n; i++) {
      if (i < n/2) left[j++] = A[i];
      else right[k++] = A[i];
    }

    System.out.println("left: " + Arrays.toString(left) + ", right: " + Arrays.toString(right));
    left = mergeSort(left);
    right = mergeSort(right);
    return merge(left, right);
  }

  private static int[] merge(int[] left, int[] right) {
    int[] res = new int[left.length + right.length];
    int i = 0, j = 0, k = 0;

    while( i < left.length && j < right.length) {
      if (left[i] < right[j]) res[k++] = left[i++];
      else res[k++] = right[j++];
    }
    while (i < left.length) res[k++] = left[i++];
    while (j < right.length) res[k++] = right[j++];

    System.out.println("merge: left " + Arrays.toString(left) + " with right " +
        Arrays.toString(right) + " results into " + Arrays.toString(res));
    return res;
  }

  public static void main(String[] args) {
    int[] A = {0, 2, 3, 2, 3, 4};
    System.out.println("Before sort: " + Arrays.toString(A));
    A = mergeSort(A);
    System.out.println("After merge sort: " + Arrays.toString(A));
  }
}
