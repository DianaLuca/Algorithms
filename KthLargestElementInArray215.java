package LeetCodeAlgorithms;

import java.util.ArrayList;
import java.util.Random;

/**
 * Find the kth largest element in an unsorted array.
 * Note that it is the kth largest element in the sorted order, not the kth distinct element.
 * For example,
 * Given [3,2,1,5,6,4] and k = 2, return 5.
 * Note:
 * You may assume k is always valid, 1 ≤ k ≤ array's length.
 *
 *  Created by dianaluca on 10/25/16.
 */

public class KthLargestElementInArray215 {

  /**
   * Solution 1: O(N) memory, avg O(N) time complexity:
   */

  //transform an arrayList to an array
  public static int[] toList(ArrayList<Integer> l) {
    int[] res = new int[l.size()];
    for(int i = 0; i < l.size(); i++){
      res[i] = l.get(i);
    }
    return res;
  }

  public static int findKthLargest1(int[] nums, int k) {
    if  (nums.length == 1) {
      assert (k == 1);
      return nums[0];
    }

    //are all equals?
    boolean bool = true;
    for(int i = 1; i < nums.length; i++) {
      if (nums[0] != nums[i]) bool = false;
    }
    if(bool == true) return nums[0];

    //choose a random pivot from nums list
    int rdm = new Random().nextInt(nums.length);
    int pivot = nums[rdm];

    //split nums into l (left arrayList) and r (right arrayList)
    ArrayList<Integer> l = new ArrayList<Integer>();
    ArrayList<Integer> r = new ArrayList<Integer>();
    for(int i = 0; i < nums.length; i++) {
      if (nums[i] >= pivot) l.add(nums[i]);
      else r.add(nums[i]);
    }

    //quick select sort
    if(k < l.size()) {
      int[] lst = toList(l);
      return findKthLargest1(lst, k);
    } else if(k > l.size()){
      int[] rst = toList(r);
      return findKthLargest1(rst, k-l.size());
    } else {
      int[] res = toList(l);
      int min = Integer.MAX_VALUE;
      for(int i = 0; i < res.length;i++) {
        if (res[i] < min) min = res[i];
      }
      return min;
    }
  }

  /**
   * Solution 2: in place memory, avg O(N) time complexity:
   */

  public static int findKthLargest2(int[] a, int k) {
    int n = a.length;
    int p = quickSelect(a, 0, n - 1, n - k + 1);
    return a[p];
  }

  public static int quickSelect(int[] a, int lo, int hi, int k) {
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

  public static void swap(int[] a, int i, int j) {
    int tmp = a[i];
    a[i] = a[j];
    a[j] = tmp;
  }

  // Test Client:
  public static void main(String[] args) {
    int[] a = {2, 7, 8, 4, 5}; //{2, 4, 5, 7, 8}
    int k = 4;
    int res1 = findKthLargest1(a, k);
    int res2 = findKthLargest2(a, k);
    System.out.printf("The %d'th bigger element from a[] is: %d",k,res1);
    System.out.printf("\nThe %d'th bigger element from a[] is: %d",k,res2);
  }
}
