package Algorithms.related;

/**
 * Edit distance is so named because it can also be thought of as the minimum number of
 * edits—insertions, deletions, and substitutions of characters—needed to transform the first
 * string into the second. For instance, the alignment shown on the left corresponds to three
 * edits: insert U, substitute O → N, and delete W.
 *
 * Created by dianaluca on 11/29/16.
 */

public class EditDistance {
  public static int[][] E;
  public static int N, M;
  public static int cnt = 0;

  public static void main(String[] args) {
    String s1 = "polynomial"; //if s1 = "polynomial" => minED = 6
    String s2 = "exponential";
    N = s1.length();
    M = s2.length();
    // iterative: dynamic programing
    E = new int[N + 1][M + 1];
    int minEditsI = iterative(s1, s2);
    System.out.println("Iterative solution: minimum nr of edits (delete, remove, change) is: " + minEditsI);

    // recursive: memoization
    for (int i = 0; i <= N; i++) {
      for (int j = 0; j <= M; j++) {
        E[i][j] = M + N;
      }
    }
    int minEditsR = recursive(s1, N, s2, M);
    System.out.println("\n\nRecursive solution with memoization: minimum nr of edits (delete, remove, change) is: " + minEditsR);
    System.out.printf("Through memoization %d recursive steps where avoided, " +
                      "being done in O(1) for 2 strings of %d and %d lengths.",cnt,N,M);
  }

  public static int recursive(String s1, int r1, String s2, int r2) {
    if (r1 == 0 && r2 == 0) return 0;

    //check if the solution is already computed
    if (E[r1][r2] != M + N) {
      System.out.printf("\nE[%d][%d] already computed",r1,r2);
      cnt++;
      return E[r1][r2];
    }

    //compute the solution
    int res = 0;
    if (r1 == 0) res = r2;
    else if (r2 == 0) res = r1;
    else res = Math.min( Math.min(1 + recursive(s1, r1, s2, r2-1), 1 + recursive(s1, r1-1, s2, r2)) ,
                        diff(s1.charAt(r1 - 1),s2.charAt(r2 - 1)) + recursive(s1, r1-1, s2, r2-1));

    return E[r1][r2] = res;
  }

  public static int iterative(String s1, String s2) {
    for (int i = 0; i <= N; i++)
      E[i][0] = i;
    for (int j = 1; j <= M; j++)
      E[0][j] = j;
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= M; j++) {
        E[i][j] = Math.min(Math.min(1 + E[i][j-1], 1 + E[i-1][j]),
                           diff(s1.charAt(i-1),s2.charAt(j-1)) + E[i-1][j-1]);
      }
    }
    return E[N][M];
  }

  public static int diff(char i, char j) {
    return i == j ? 0 : 1;
  }
}
