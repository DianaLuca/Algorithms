package Algorithms.Leetcode;

import java.util.ArrayList;
import java.util.List;

/** l
 * left -> right -> root
 * Created by dianaluca on 10/5/16.
 */

public class BinaryTreePostorderTraversal145 {
  public class TreeNode {
         int val;
         TreeNode left;
         TreeNode right;
         TreeNode(int x) { val = x; }
    }


  List<Integer> postOrd = new ArrayList<>();

  public List<Integer> postorderTraversal(TreeNode root) {
    if(root == null) return postOrd;

    postorderTraversal(root.left);
    postorderTraversal(root.right);
    postOrd.add(root.val);

    return postOrd;
  }
}
