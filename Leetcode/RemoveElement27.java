package Algorithms.Leetcode;

/**
 * Given an array and a value, remove all instances of that value in place and return the new length.
 * Do not allocate extra space for another array, you must do this in place with constant memory.
 * The order of elements can be changed. It doesn't matter what you leave beyond the new length.
 *
 * Example: Given input array nums = [3,2,2,3], val = 3,
 * Your function should return length = 2, with the first two elements of nums being 2.
 *
 * Created by dianaluca on 10/3/16.
 */

public class RemoveElement27 {
  public static int removeElement(int[] nums, int val) {
    int numsLen = nums.length;
    int i = 0;
    int j = numsLen - 1;

    while (i < numsLen && j >=0) {
      if (nums[i] == val && nums[j] != val) {
        nums[i] = nums[j];
        i++;
        j--;
        numsLen--;
      } else if (nums[i] == val && nums[j] == val) {
        j--;
        numsLen--;
      }
      else    i++;
    }
    return numsLen;
  }

  public static void main(String[] args) {
    int[] nums = {3, 2, 2, 3};
    int val = 3;
    System.out.println(removeElement(nums, val));  //print 2
  }
}
