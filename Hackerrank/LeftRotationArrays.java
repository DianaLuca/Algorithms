package Algorithms.Hackerrank;

import java.util.Scanner;

/**
 * A left rotation operation on an array of size n shifts each of the array's elements 1 unit to the left.
 *
 * https://www.hackerrank.com/challenges/ctci-array-left-rotation
 *
 * Created by dianaluca on 11/15/16.
 */

public class LeftRotationArrays {
  public static int[] arrayLeftRotation(int[] a, int n, int k) {
    int[] firstk = new int[k];
    for(int i = 0; i < k; i++) {
      firstk[i] = a[i];
    }
    System.arraycopy(a, k, a, 0, n-k);
    System.arraycopy(firstk, 0, a, n-k, k);
    return a;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(); //array length
    int k = in.nextInt(); //rotation
    int a[] = new int[n];
    for(int a_i=0; a_i < n; a_i++){
      a[a_i] = in.nextInt();
    }

    int[] output = new int[n];
    output = arrayLeftRotation(a, n, k);
    for(int i = 0; i < n; i++)
      System.out.print(output[i] + " ");

    System.out.println();

  }
}
