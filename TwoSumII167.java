package LeetCodeAlgorithms;

import java.util.Arrays;

/**
 * Given an array of integers that is already sorted in ascending order,
 * find two numbers such that they add up to a specific target number.
 *
 * The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
 * Please note that your returned answers (both index1 and index2) are not zero-based.
 *
 * You may assume that each input would have exactly one solution.
 *
 * Created by dianaluca on 11/11/16.
 */

public class TwoSumII167 {
  public static int binarySearch(int[] numbers, int lo, int hi, int element) {
    int N = numbers.length;
    if (lo > hi) return -1;

    int mid = lo + (hi-lo)/2;

    if (element < numbers[mid]) return binarySearch(numbers, lo, mid-1, element);
    else if (element > numbers[mid]) return binarySearch(numbers, mid+1, hi, element);
    else return mid;
  }

  public static int[] twoSum(int[] numbers, int target) {
    int i = 0;
    int N = numbers.length;

    while (i < N) {
      int element = target - numbers[i];
      int pos = binarySearch(numbers, i+1, N-1, element);

      if (pos != -1 ) return new int[] {i+1, pos+1};
      i++;
    }

    return null;
  }

  /**
   * Input: numbers = {2, 7, 11, 15}
   *        target = 9
   * Output: [1, 2]
   * index1 = 1, index2 = 2
   */

  public static void main(String[] args) {
    int[] arr = {2, 7, 11, 15};
    int targhet = 9;
    System.out.println(Arrays.toString(twoSum(arr, targhet)));
  }
}
