package LeetCodeAlgorithms;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Given a binary tree, return the level order traversal of its nodes' values.
 * (ie, from left to right, level by level).
 * For example:
 * Given binary tree [3,9,20,null,null,15,7],
 *      3
 *     / \
 *    9  20
 *      /  \
 *     15   7
 * return it's level order traversal as:
 *
 * [
 *  [3],
 *  [9, 20],
 *  [15, 7]
 * ]
 *
 * Created by dianaluca on 9/30/16.
 */

public class BinaryTreeLevelOrderTraversal102 {
  public static class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) {
      val = x;
    }
  }

  public static List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<List<Integer>>();
    if (root == null) return result;
    return levelOrder(root, 0, result);
  }

  private static List<List<Integer>> levelOrder(TreeNode root, int level, List<List<Integer>> result) {
    if (result.size() <= level) result.add(level, new ArrayList<Integer>());
    result.get(level).add(root.val);
    if (root.left != null) levelOrder(root.left, level + 1, result);
    if (root.right != null) levelOrder(root.right, level + 1, result);
    return  result;
  }

  //TestClient:
  public static void main(String[] args) {
    TreeNode root = new TreeNode(3);
    root.left = new TreeNode(9);
    root.right = new TreeNode(20);
    root.right.left = new TreeNode(15);
    root.right.right = new TreeNode(7);
    root.right.right.left = new TreeNode(30);
    root.right.right.right = new TreeNode(50);

    List<List<Integer>> levelOrderList = levelOrder(root);
    System.out.println(Arrays.asList(levelOrderList));

    // ----------- reverse the "levelOrderList" List of Lists (see ex: 107) -------------

    List<List<Integer>> reverse = levelOrderList;
    int N = reverse.size();
    int i = 0;
    int j = N - i - 1;
    while (i <= j) {
      List<Integer> arrEl = reverse.get(i);
      reverse.set(i, reverse.get(j));
      reverse.set(j, arrEl);
      i++;
      j--;
    }
    System.out.println(Arrays.asList(reverse));

  }
}
