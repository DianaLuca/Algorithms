package Algorithms.related;

import java.util.Arrays;

/**
 * Sort an array in ascending order
 *
 * Created by dianaluca on 11/19/16.
 */

public class BubbleSort {
  public static void main(String[] args) {
    int[] arr = {7, 3, 2, 1, 0, 1, 0, 1, 9};
    bubbleSort(arr);
    System.out.println(Arrays.toString(arr));
  }

  public static void bubbleSort(int[] arr){
    int N = arr.length;
    boolean flag = true;

    while(flag) {
      flag = false;

      for (int i = 0; i < N-1; i++) {
        if (arr[i] > arr[i+1]) {
          swap(arr, i, i+1);
          flag = true;
        }
      }
    }
  }

  private static void swap(int[] arr, int i, int j) {
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
  }
}
