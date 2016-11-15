package Algorithms.Leetcode;

import java.util.HashMap;

/**
 * Given a binary tree, determine if it is height-balanced.
 * For this problem, a height-balanced binary tree is defined as a binary tree
 * in which the depth of the two subtrees of every node never differ by more than 1.
 *
 * Created by dianaluca on 10/5/16.
 */

public class BalancedBinaryTree110 {
  public class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) {val = x;}
  }

  HashMap<TreeNode, Integer> cache = new HashMap <TreeNode, Integer>();

  public boolean isBalanced(TreeNode root) {
    if  (root == null)  return true;    //tree is empty
    int leftHeight = treeHeight(root.left);
    int rightHeight = treeHeight(root.right);
    if (Math.abs(leftHeight - rightHeight) > 1) return false;

    return isBalanced(root.left) && isBalanced(root.right) && (Math.abs(leftHeight - rightHeight) <= 1);
  }

  private int treeHeight(TreeNode root) {
    if (root == null) return 0;

    if (cache.containsKey(root))
      return cache.get(root);

    int result = 1 + Math.max(treeHeight(root.left), treeHeight(root.right));
    cache.put (root, result);
    return result;
  }
}
