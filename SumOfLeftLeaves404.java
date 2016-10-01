package LeetCodeAlgorithms;

/**
 * Given binary tree [3,9,20,null,null,15,7],
 *      3
 *     / \
 *    9  20
 *      /  \
 *     15   7
 *
 * return sum = 9 + 15
 *
 * Created by dianaluca on 10/1/16.
 */

public class SumOfLeftLeaves404 {
  public static class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) {
      val = x;
    }
  }

  public static int sumOfLeftLeaves(TreeNode root) {
    int sum = 0;
    if (root == null)  return sum;
    if (root.left != null && root.left.left == null && root.left.right == null) sum += root.left.val;
    if (root.left != null) sum += sumOfLeftLeaves(root.left);
    if (root.right != null) sum += sumOfLeftLeaves(root.right);
    return sum;
  }

  //TestClient:
  public static void main(String[] args) {
    TreeNode root = new TreeNode(3);
    root.left = new TreeNode(9);
    root.right = new TreeNode(20);
    root.right.left = new TreeNode(15);
    root.right.right = new TreeNode(7);

    int sum  = sumOfLeftLeaves(root);
    System.out.println(sum); //print 24
  }
}
