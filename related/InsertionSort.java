package Algorithms.related;

import java.util.Arrays;

/**
 * Created by dianaluca on 10/26/16.
 */
public class InsertionSort {

  private static int cnt = 0;

  public static void insertionSort(int[] A) {
    int n = A.length;
    for (int i = 0; i < n; i++) {
      int x = A[i];
      int j = i-1;
      while (j >= 0 && A[j] > x) {
        cnt++;
        A[j+1] = A[j];
        j-- ;
      }
      A[j+1] = x;
    }
  }

  //Test Client for insertionSort()
  public static void main(String[] args) {
    //sort array A using insertion stort algorithm
    int[] A = {7, 4, 6, 5, 4, 10};
    System.out.println("Initial array " + Arrays.toString(A));
    insertionSort(A);
    System.out.println("After insertion sort A: " + Arrays.toString(A) + " in " + cnt + " steps.");
  }
}
