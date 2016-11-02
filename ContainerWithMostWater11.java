package LeetCodeAlgorithms;

/**
 * Created by dianaluca on 11/1/16.
 */
public class ContainerWithMostWater11 {

  //O(N)
  public static int maxArea(int[] height) {
    int res = Integer.MIN_VALUE;
    int N = height.length;
    int i = 0, j = N-1;

    while (i < j ) {
      res = Math.max( res, Math.min(height[i],height[j]) * (j-i) );
      if (height[i] < height[j]) i++;
      else j--;
    }
    return res;
  }

  //O(N^2)
  public static int maxAreaNN(int[] height) {
    int res = Integer.MIN_VALUE;
    for (int i = 0; i < height.length; i++) {
      int j = height.length - 1;
      while (j>i) {
        res = Math.max( res, (Math.min(height[i],height[j]) ) * (j-i) );
        j--;
      }
    }
    return res;
  }

  //
  public static void main(String[] args) {
    int[] a = {1,2,3,4,5,6,7,8,9,10};
    System.out.println(maxArea(a));
  }
}
