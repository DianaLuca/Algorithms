package LeetCodeAlgorithms;

/**
 * Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
 * Example:
 * (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
 * (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].
 *
 * Note:
 * You may assume all input has valid answer.
 *
 * Follow Up:
 * Can you do it in O(n) time and/or in-place with O(1) extra space?
 *
 * Created by dianaluca on 10/26/16.
 */

public class WiggleSortII324 {
  public void wiggleSort(int[] nums) {
    if (nums.length <= 1) return;
    int n = nums.length;
    int k = (n+1)/2; //the k'th largest element from nums
    int val = findKthLargest2(nums, k); //find the value of the k'th smaller element

    /**
     * nums = {<= val, <= val, ....*N/2, val, >val, >val, ....*N/2, >val}
     *
     * step by step - index mapping:
     * https://discuss.leetcode.com/topic/41464/step-by-step-explanation-of-index-mapping-in-java
     */
    int left = 0, i = 0, right = n - 1;

    while (i <= right) {

      if (nums[newIndex(i,n)] > val) {
        swap(nums, newIndex(left++,n), newIndex(i++,n));
      }
      else if (nums[newIndex(i,n)] < val) {
        swap(nums, newIndex(right--,n), newIndex(i,n));
      }
      else {
        i++;
      }
    }
  }

  private int newIndex(int index, int n) {
    System.out.printf("\nindex %d, n %d, result: new index: %d",index,n,(1 + 2*index) % (n | 1));
    return (1 + 2*index) % (n | 1);
  }


  public int findKthLargest2(int[] a, int k) {
    int n = a.length;
    int p = quickSelect(a, 0, n - 1, n - k + 1);
    return a[p];
  }

  public int quickSelect(int[] a, int lo, int hi, int k) {
    int i = lo, j = hi, pivot = a[hi];
    while(i < j) {
      if (a[i++] > pivot) swap(a, --i, --j);
    }
    swap(a, i, hi);

    int m = i - lo + 1;  //m = number of element slower than pivot
    if (k == m) return i;
    else if (k < m) return quickSelect(a, lo, i-1, k);
    else  return quickSelect(a, i+1, hi, k-m);  //since k > m, it will be the k-m'th element in a[i+1, hi] subarray
  }

  public void swap(int[] a, int i, int j) {
    int tmp = a[i];
    a[i] = a[j];
    a[j] = tmp;
  }
}
