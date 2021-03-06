package Algorithms.Leetcode;

/**
 * Given two binary trees, write a function to check if they are equal or not.
 * Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
 *
 * Created by dianaluca on 9/14/16.
 */

public class SameTree100 {
  public class TreeNode {
         int val;
         TreeNode left;
         TreeNode right;
         TreeNode(int x) { val = x; }
  }

  public boolean isSameTree(TreeNode p, TreeNode q) {

    if (p == null || q == null) {
      if (p == null && q == null)
        return true;
      else
        return false;
    }
    if (p.val != q.val ) return false;
    else {
      return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }

  }

  public static void main() {}


}
