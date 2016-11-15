package Algorithms.Leetcode;

import java.util.Arrays;

/**
 * Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
 * You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
 * The number of elements initialized in nums1 and nums2 are m and n respectively.
 *
 * Created by dianaluca on 10/29/16.
 */

public class MergeSortedArray88 {
  /**
   *  memory: in place
   */

  public static void merge(int[] nums1, int m, int[] nums2, int n) {
    int i=0, j=0;

    while (i<m && j<n) {
      while (i<m && nums1[i] > nums2[j]) {
        //switch elements btw nums1[i] <=> nums2[j]
        int tmp1 = nums1[i];
        nums1[i++] = nums2[j];
        nums2[j] = tmp1;

        int k = j+1;
        while (k < n && nums2[k] < nums2[k-1]){
          //switch elements inside nums2 till they are in ascending order
          int tmp2 = nums2[k-1];
          nums2[k-1] = nums2[k];
          nums2[k++] = tmp2;
        }
      }
      if (i<m && nums1[i] <= nums2[j]) i++;
    }

    while (i < (n + m) && j < n) {
      nums1[i++] = nums2[j++];
    }
    System.out.println(Arrays.toString(nums1));
  }

  /**
   *  O(N) additional memory
   */

  public static void mergeN(int[] nums1, int m, int[] nums2, int n) {
    int[] res = new int[m+n];

    int i=0, j=0, k=0;
    while (i<m && j<n) {
      if  (nums1[i] < nums2[j]) res[k++] = nums1[i++];
      else res[k++] = nums2[j++];
    }
    while (i<m) {
      res[k++] = nums1[i++];
    }
    while (j<n) {
      res[k++] = nums2[j++];
    }
    nums1 = res;
    System.out.println(Arrays.toString(nums1));
  }

  public static void main(String[] args) {
    int[] nums1 = {0,2,3,5,7,0,0,0,0}; //m=5
    int[] nums2 = {1,2,3,4}; //n=4
    int n = nums2.length;
    int m = nums1.length - n;
    merge(nums1, m, nums2, n);
    //mergeN(nums1, m, nums2, n);
  }
}
