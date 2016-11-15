package Algorithms.Leetcode;

import java.util.Arrays;
import java.util.List;

/**
 * Given an index k, return the k'th row of the Pascal's triangle.
 * For example, given k = 3, return: [1, 3, 3, 1]
 * Note: could you optimize your algorithm to use only
 * O(k) extra space?
 *
 * Created by dianaluca on 10/10/16.
 */

public class PascalsTriangleII119 {
  public List<Integer> getRow(int rowIndex) {
    // C(n, k) = C(n, k-1) * ( (n - (k - 1) )/ k )
    // rowIndex - is n; i - is k
    Integer[] rowList = new Integer[rowIndex + 1];
    rowList[0] = 1;
    for (int i = 1; i <= rowIndex; i++) {
      rowList[i] = rowList[i-1] * ( (rowIndex - (i-1) ) / i );
    }
    return Arrays.asList(rowList);
  }
}
