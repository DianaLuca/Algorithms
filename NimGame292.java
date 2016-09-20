package LeetCode;

/**
 * There is a heap of stones on the table,
 * each time one of you take turns to remove 1 to 3 stones.
 * The one who removes the last stone will be the winner.
 * You will take the first turn to remove the stones.

 * Write a function to determine whether you can win the game given the number of stones in the heap.
 * For example,
 * if there are 4 stones in the heap, then you will never win the game:
 * no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

 * Created by dianaluca on 9/15/16.
 */

public class NimGame292 {
  public boolean canWinNim(int n) {
    if (n % 4 == 0) return false;
    else return true;
  }
}
