package LeetCodeAlgorithms;

import java.util.ArrayList;
import java.util.List;

/**
 * Given a binary tree, return all root-to-leaf paths.
 * For example, given the following binary tree:
 *      1
 *    /   \
 *   2     3
 *    \
 *     5
 *
 * All root-to-leaf paths are:
 * ["1->2->5", "1->3"]
 *
 * Created by dianaluca on 10/12/16.
 */

public class BinaryTreePaths257 {
  public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
  }

  public List<String> binaryTreePaths(TreeNode root) {
    List<String> allPaths = new ArrayList<String>();
    StringBuilder path = new StringBuilder();
    dfs(root, path, allPaths);
    return allPaths;
  }

  public void dfs(TreeNode root, StringBuilder path, List<String> allPaths) {
    if (root == null) return;

    int len = path.length(); // 0
    if (root.left == null && root.right == null) {  //leaf
      path.append(root.val);
      allPaths.add(path.toString());
      path.setLength(len); // restart StringBuilder "path" to length 0 since we met a leaf
      return;
    }

    path.append(root.val).append("->");
    dfs(root.left, path, allPaths);
    dfs(root.right, path, allPaths);
    path.setLength(len);
  }
}
