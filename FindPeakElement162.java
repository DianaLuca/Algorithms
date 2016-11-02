package LeetCodeAlgorithms;

/**
 * A peak element is an element that is greater than its neighbors.
 * Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
 * The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
 * You may imagine that num[-1] = num[n] = -∞.
 * For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
 *
 * Created by dianaluca on 11/2/16.
 */

public class FindPeakElement162 {

  /**
   * Solution1: Time Complexity O(logN)
   */
  public int findPeakElement(int[] nums) {
    // given: num[i] ≠ num[i+1]
    int N = nums.length;
    int left = 0;
    int right = N-1;
    return findPeakElementLR(nums, left, right);
  }

  public int findPeakElementLR(int[] nums, int left, int right) {
    int mid = left + (right-left)/2;
    boolean smallerThanLeft = (mid - 1 >= left) && (nums[mid - 1] > nums[mid]);
    boolean smallerThanRight = (mid + 1 <= right) && (nums[mid] < nums[mid + 1]);

    if (left > right) return -1;

    if (!smallerThanLeft && !smallerThanRight)
      return mid;
    else if (smallerThanLeft)
      return findPeakElementLR(nums, left, mid-1);
    else //smallerThanRight
      return findPeakElementLR(nums, mid+1, right);
  }


  /**
   * Solution2: Time Complexity O(N)
   */
  public int findPeakElementN(int[] nums) {
    // given: num[i] ≠ num[i+1]
    int N = nums.length;
    if (N == 1 || nums[0] > nums[1]) return 0;
    if (N == 2 && nums[0] < nums[1]) return 1;

    // N >= 3
    int i = 0, j = i + 1;
    while(j < N && nums[i] < nums[j]) {
      i++;
      j++;
    }
    // touched the end of the array and still ascending
    if (j == N-1 && nums[i] < nums[j] ) return j;
      // somewhere inside array : nums[i] > nums[j]
    else return i;
  }
}
