package Algorithms.Codility;

import java.util.Arrays;

/**
 * A non-empty zero-indexed array A consisting of N integers is given.
 * The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).
 *
 * Maximize A[P]*A[Q]*A[R] for any triplet(P,Q,R)
 *
 * Created by dianaluca on 11/12/16.
 */

public class SortingMaxProductOfThree {
  public static int solution(int[] A) {
    if (A.length <= 2) return -1;

    Arrays.sort(A);
    return Math.max(A[0]*A[1]*A[A.length-1], A[A.length-3]*A[A.length-2]*A[A.length-1]);
  }

  public static void main(String[] args) {
    int[] A = {-1000, 1, 5, 3, 2, -1000, 0, 1000, 100, 50, -70, 1000};
    System.out.println(solution(A));
  }
}
