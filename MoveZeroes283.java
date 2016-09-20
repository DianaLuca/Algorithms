package LeetCode;

/**
 * Given an array nums, write a function to move all 0's to the end of it
 * while maintaining the relative order of the non-zero elements.
 * For example,
 * given nums = [0, 1, 0, 3, 12], after calling your function,
 * nums should be [1, 3, 12, 0, 0].

 Note:
 * You must do this in-place without making a copy of the array.
 * Minimize the total number of operations.

 * Created by dianaluca on 9/15/16.
 */

public class MoveZeroes283 {
  public void moveZeroes(int[] nums) {
    int N = nums.length;

    // Method1: O(N^2) - & - in place memory
    // for(int i = 0; i < N-1; i++) {
    //     if(nums[i] == 0) {
    //         int nz = i+1;

    //         if (nums[nz] == 0) {
    //             while(nz < N-1 && nums[nz] == 0) {
    //                 ++nz;
    //             }
    //             int tmp = nums[i];
    //             nums[i] = nums[nz];
    //             nums[nz] = tmp;
    //         }
    //         else if(nz < N) {
    //             int tmp = nums[i];
    //             nums[i] = nums[nz];
    //             nums[nz] = tmp;
    //         }
    //     }
    // }


    //Method 2: O(N) - & - in place memory

    int n = 0;

    for (int i = 0; i < N; ++i) {
      if (nums[i] != 0) {
        nums[n++] = nums[i];
      }
    }

    for (int i = n; i < N; ++i) {
      nums[i] = 0;
    }
  }
}
