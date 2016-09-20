package LeetCode;

/**
 * Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
 * Do not allocate extra space for another array,
 * you must do this in place with constant memory.
 * For example, Given input array nums = [1,1,2],
 * Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
 * It doesn't matter what you leave beyond the new length.
 *
 * Created by dianaluca on 9/18/16.
 */

public class RemoveDuplicatesSortedArray26 {
  public int removeDuplicates(int[] nums) {
    int N = nums.length;
    int piv = 0;
    for(int i = 0; i < N; i++){
      if(i == 0 || nums[i] > nums[i-1]){
        nums[piv++] = nums[i];
      }
    }
    return piv;
  }
}
