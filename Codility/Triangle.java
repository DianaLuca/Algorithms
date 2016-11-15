package Algorithms.Codility;
import java.util.Arrays;

/**
 * Determine whether a triangle can be built from a given set of edges.
 * A zero-indexed array A consisting of N integers is given.
 *
 * A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:
 * A[P] + A[Q] > A[R],
 * A[Q] + A[R] > A[P],
 * A[R] + A[P] > A[Q].
 *
 * N is an integer within the range [0..100,000];
 * each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
 *
 * Created by dianaluca on 11/13/16.
 */

public class Triangle {
  public int solution(int[] A) {
    Arrays.sort(A);
    for (int i = 0; i < A.length-2; i++) {
      if ((long)A[i] + (long)A[i+1] > (long)A[i+2] && (long)A[i] + (long)A[i+2] > (long)A[i+1] && (long)A[i+1] + (long)A[i+2] > (long)A[i])
        return 1;
    }
    return 0;
  }
}
