package Algorithms.Leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * * Given a binary tree, return the level order traversal of its nodes' values.
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
 *  [15, 7],
 *  [9, 20],
 *  [3]
 * ]
 *
 *
 * Created by dianaluca on 10/1/16.
 */

public class BinaryTreeLevelOrderTraversalII107 {
  public static class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) {
      val = x;
    }
  }

  public static List<List<Integer>> levelOrderBottom(TreeNode root) {
    List<List<Integer>> response = new ArrayList<List<Integer>>();
    if  (root == null) return response;
    List<List<Integer>> upsideDownResponse = levelOrderBottom(root, 0, response);

    List<List<Integer>> bottomUpResponse = upsideDownResponse;
    int i = 0;
    int j = bottomUpResponse.size() - 1;
    while (i <= j) {
      List<Integer> lst = bottomUpResponse.get(i);
      bottomUpResponse.set(i, bottomUpResponse.get(j));
      bottomUpResponse.set(j, lst);
      i++;
      j--;
    }
    return bottomUpResponse;
  }

  public static List<List<Integer>> levelOrderBottom(TreeNode root, int level, List<List<Integer>> response) {
    if  (response.size() <= level) response.add(level, new ArrayList<Integer>());
    response.get(level).add(root.val);
    if  (root.left != null) levelOrderBottom(root.left, level + 1, response);
    if  (root.right != null) levelOrderBottom(root.right, level + 1, response);
    return response;
  }

  //TestClient:
  public static void main(String[] args) {
    TreeNode root = new TreeNode(3);
    root.left = new TreeNode(9);
    root.right = new TreeNode(20);
    root.right.left = new TreeNode(15);
    root.right.right = new TreeNode(7);

    List<List<Integer>> levelOrderList = levelOrderBottom(root);
    System.out.println(Arrays.asList(levelOrderList));
  }
}
