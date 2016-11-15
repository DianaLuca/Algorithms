package Algorithms.Leetcode;

/**
 * Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
 * with the colors in the order red, white and blue.
 * Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
 * Note:
 * You are not suppose to use the library's sort function for this problem.
 *
 * See: Dutch national flag problem:
 * https://en.wikipedia.org/wiki/Dutch_national_flag_problem
 *
 * Created by dianaluca on 10/26/16.
 */

public class SortColors75 {
  public void sortColors(int[] nums) {
    if (nums.length < 2) return;
    int mid = 1;
    int i = 0, j = 0;
    int n = nums.length-1;

    //i - maximum index of 0's; j - carry variable; n - minimum index of 2's
    while (j <= n) {
      if(nums[j] < mid){
        swap(nums, j, i);
        i++; j++;
      } else if (nums[j] > mid) {
        swap(nums, j, n);
        n--;
      } else { //nums[j] == mid
        j++;
      }
    }
  }
  public void swap (int[] A, int i, int j) {
    int tmp = A[i];
    A[i] = A[j];
    A[j] = tmp;
  }
}
