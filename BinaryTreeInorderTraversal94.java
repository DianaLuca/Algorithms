package LeetCodeAlgorithms;

import java.util.ArrayList;
import java.util.List;

/**
 * Given a binary tree, return the inorder traversal of its nodes' values.
 * For example:
 * Given binary tree [1,null,2,3],
 *   1
 *    \
 *     2
 *    /
 *   3
 * return [1,3,2].
 * Note: Recursive solution is trivial, could you do it iteratively?
 *
 * Created by dianaluca on 10/5/16.
 */

public class BinaryTreeInorderTraversal94 {
  public class TreeNode {
         int val;
         TreeNode left;
         TreeNode right;
         TreeNode(int x) { val = x; }
    }

  List<Integer> inOrd = new ArrayList<>();
  public List<Integer> inorderTraversal(TreeNode root) {
    if (root == null) return inOrd;

    inorderTraversal(root.left);
    inOrd.add(root.val);
    inorderTraversal(root.right);

    return inOrd;
  }
}
