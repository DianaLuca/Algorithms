package Algorithms.Leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * root -> left -> right
 * Created by dianaluca on 10/5/16.
 */

public class BinaryTreePreorderTraversal144 {
  public class TreeNode {
         int val;
         TreeNode left;
         TreeNode right;
         TreeNode(int x) { val = x; }
     }

  public class Solution {
    List<Integer> preOrd = new ArrayList<>();

    public List<Integer> preorderTraversal(TreeNode root) {
      if (root == null) return preOrd;
      preOrd.add(root.val);
      preorderTraversal(root.left);
      preorderTraversal(root.right);

      return preOrd;
    }
  }
}
