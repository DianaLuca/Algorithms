package Algorithms.Hackerrank;
import java.util.*;

/**
 * Created by dianaluca on 11/20/16.
 */
public class BubbleSort {
  /**
   * Sample Input 0

   3
   1 2 3

   Sample Output 0

   Array is sorted in 0 swaps.
   First Element: 1
   Last Element: 3

   */
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int a[] = new int[n];
    for(int a_i=0; a_i < n; a_i++){
      a[a_i] = in.nextInt();
    }
    bubbleSort(a);
    System.out.println("First Element: " + a[0]);
    System.out.println("Last Element: " + a[n-1]);
  }

  public static void bubbleSort(int[] a) {
    int N = a.length;
    int totalNrSwaps = 0;

    for(int i = 0; i < N; i++) {
      int nrOfSwaps = 0;

      for(int j = 0; j < N-1; j++) {
        if(a[j] > a[j+1]) {
          swap(a, j, j+1);
          nrOfSwaps++;
        }
      }
      totalNrSwaps += nrOfSwaps;

      if(nrOfSwaps == 0) {
        System.out.println("Array is sorted in " + totalNrSwaps + " swaps.");
        break;
      }
    }
  }

  public static void swap(int[] a, int x, int y) {
    int tmp = a[x];
    a[x] = a[y];
    a[y] = tmp;
  }
}
