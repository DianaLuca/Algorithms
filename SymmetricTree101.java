package LeetCodeAlgorithms;

import java.util.LinkedList;
import java.util.Queue;

/**
 * Given a binary tree check if whether it is a mirror of itself (symmetric around itself)
 *
 * For example: [1, 2,2, 3,4,4,3]
 *      1
 *     / \
 *    2   2
 *   / \ / \
 *  3  4 4  3
 *
 * Created by dianaluca on 10/4/16.
 */

public class SymmetricTree101 {
  public static class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) {
      val = x;
    }
  }

  /*
   ------- RECURSIVE ---------
   */
  public static boolean areSymetric(TreeNode nL, TreeNode nR) { //recursive
    if (nL == null || nR == null) return nL == nR;
    return (nL.val == nR.val) && areSymetric(nL.left, nR.right) && areSymetric(nL.right, nR.left);
  }

  public static boolean isSymmetric(TreeNode root) { //recursive
    if (root == null) return false;
    return areSymetric(root.left, root.right);
  }

  /*
   -------- ITERATIVE ---------
   */
  public static boolean isSymmetricIterative(TreeNode root) {
    if (root == null) return false;

    Queue<TreeNode> queue = new LinkedList<>();
    queue.add(root);
    queue.add(root);

    while (!queue.isEmpty()){
      TreeNode t1 = queue.poll();
      TreeNode t2 = queue.poll();
      if (t1 == null && t2 == null) continue;
      if (t1 == null || t2 == null) return false;
      if (t1.val != t2.val) return false;
      queue.add(t1.left);
      queue.add(t2.right);
      queue.add(t1.right);
      queue.add(t2.left);
    }
    return true;
  }

  //Test Client:
  public static void main(String[] args){
    TreeNode root = new TreeNode(1);
    root.left = new TreeNode(2);
    root.right = new TreeNode(2);
    root.left.left = new TreeNode(3);
    root.left.right = new TreeNode(4);
    root.right.left = new TreeNode(4);
    root.right.right = new TreeNode(3);

    //test recursive method:
    System.out.println(isSymmetric(root)); //return true
    //replace one node with null to return false.

    //test iterative method
    System.out.println(isSymmetricIterative(root));
  }
}
