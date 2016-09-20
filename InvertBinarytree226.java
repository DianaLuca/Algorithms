package LeetCode;

/**
 * Created by dianaluca on 9/15/16.
 */
public class InvertBinarytree226 {
  public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
    }

  public TreeNode invertTree(TreeNode root) {
  if (root == null) return null;

  else {
    invertTree(root.left);
    invertTree(root.right);

    TreeNode tmp = root.right;
    root.right = root.left;
    root.left = tmp;
  }
  return root;
  }

}
