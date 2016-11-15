package Algorithms.related;

/**
 * Print on a new line each subset of a given set.
 * If you have a set of length N, print 2^N subsets(including empty set)
 *
 * Created by dianaluca on 9/21/16.
 */

public class ListSubsets {
  public static void subsets(int[] myArray) {
    int N = myArray.length;
    int allMasks = (1 << N); //allMasks = 8 (when N = 3);

    for (int i = 0; i < allMasks; i++) { // i: 0 -> 7
      for (int j = 0; j < N; j++) {  // j: 0 -> 3
        if ((i & (1 << j)) > 0)
          System.out.print(myArray[j] + " ");
      } //end for2
      System.out.println();
    } // end for1
  }

  public static void main(String[] args) {
    int[] myArray = {1, 22, 333};
    subsets(myArray);
  }
}
