package Algorithms.Codility;

import java.util.Arrays;

/**
 * Created by dianaluca on 11/12/16.
 */
public class MergeSort {
  public static void main(String[] args) {
    int[] arr = {7,8,1,0,5,3,21,20};
    System.out.println("Before mergeSort: " + Arrays.toString(arr));
    arr = mergeSort(arr);
    System.out.println("After mergeSort: " + Arrays.toString(arr));
  }

  public static int[] mergeSort(int[] arr) {
    if (arr.length <= 1) {
      return arr;
    }

    int[] left = new int[arr.length/2];
    int[] right = new int[arr.length - left.length];
    System.arraycopy(arr, 0, left, 0, left.length);
    System.arraycopy(arr, left.length, right, 0, right.length);

    mergeSort(left);
    mergeSort(right);
    merge(left, right, arr); //merge both halves together overwriting arr, return arr as result
    return arr;
  }

  public static int[] merge(int[] left, int[] right, int[] arr) {
    int i = 0, j = 0, k = 0;

    while (i < left.length && j < right.length) {
      if (left[i] < right[j]) arr[k++] = left[i++];
      else arr[k++] = right[j++];
    }
    //copy remaining elements
    System.arraycopy(left, i, arr, k, left.length - i);
    System.arraycopy(right, j, arr, k, right.length - j);

    return arr;
  }
}
