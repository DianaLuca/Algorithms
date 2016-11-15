package Algorithms.Codility;

import java.util.HashSet;
import java.util.Set;

/**
 * Compute number of distinct values in an array
 *
 * Created by dianaluca on 11/13/16.
 */

public class Distinct {
  public int solution(int[] A) {
    if (A.length == 0) return 0;
    Set<Integer> set = new HashSet<>();
    for(int i = 0; i < A.length; i++) {
      set.add(A[i]);
    }
    return set.size();
  }
}
